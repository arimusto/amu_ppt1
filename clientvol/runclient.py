from urllib import request
from hashlib import md5
from flask import Flask, send_file

data_url = "http://server.docker:5000/data"
hash_url = "http://server.docker:5000/hash"
filename = "./file.txt"

def get_file(fname: str):
    try:
        with request.urlopen(data_url) as data:
            data = data.read().decode("utf-8")
        with request.urlopen(hash_url) as hash:
            hash = hash.read().decode("utf-8")
    except:
        return False

    with open(fname, "w", encoding = "utf-8") as file:
        file.write(data)
    
    return (data, hash)

def get_hash(fname: str):
    md5hash = md5()
    with open(fname, "rb") as file:
        content = file.read()
        md5hash.update(content)

    return md5hash.hexdigest()    


app = Flask(__name__)

@app.route("/")
def hello():
    data = get_file(filename)
    if not data:
        return send_file("./error.html")

    checksum = get_hash(filename)

    page = ""
    page += "<!DOCTYPE html>\n<html lang='en'>\n<head>\n<meta charset='UTF-8'>\n<title>Hello from Client</title>\n</head>\n<body>\n"
    page += "<p>Palvelimelta noudettu data:</p>\n"
    page += f"<p>{data[0]}</p>\n"
    page += f"<p>Data tallennettu tiedostoon '{filename}'</p>\n"
    page += f"<p>Palvelimelta saatu tarkastussumma: {data[1]}</p>\n"
    page += f"<p>Paikallisen tiedoston tarkastussumma: {checksum}</p>\n"
    page += "</body>\n</html>\n"
    return page