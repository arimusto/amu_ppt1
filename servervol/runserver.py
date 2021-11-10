from random import choice
from string import ascii_letters as ltrs
from hashlib import md5
from flask import Flask, send_file

filename = "./file.txt"
hashname = "./md5hash.txt"

def create_file(fname: str):
    with open(fname, "w", encoding = "utf-8") as file:
        random_text = ""
        for _ in range(1024):
            random_text += choice(ltrs)
        file.write(random_text)

def create_hash(fname: str, hname: str):
    md5hash = md5()
    with open(fname, "rb") as file:
        content = file.read()
        md5hash.update(content)

    with open(hname, "w", encoding = "utf-8") as file:
        file.write(md5hash.hexdigest())

app = Flask(__name__)

@app.route("/")
def hello():
    return send_file("./hello.html")

@app.route("/data")
def data():
    create_file(filename)
    create_hash(filename, hashname)
    return send_file(filename)

@app.route("/hash")
def hash():
    return send_file(hashname)
