from random import choice
from string import ascii_letters as ltrs
from hashlib import md5
from flask import Flask, send_file

def create_files():
    md5hash = md5()
    with open("file.txt", "w", encoding = "utf-8") as file:
        random_text = ""
        for _ in range(1024):
            random_text += choice(ltrs)
        file.write(random_text)

    with open("file.txt", "rb") as file:
        content = file.read()
        md5hash.update(content)

    with open("md5hash.txt", "w", encoding = "utf-8") as file:
        file.write(md5hash.hexdigest())

app = Flask(__name__)

@app.route("/")
def hello():
    return send_file("./hello.html")

@app.route("/data")
def data():
    create_files()
    return send_file("./file.txt")

@app.route("/hash")
def hash():
    return send_file("./md5hash.txt")
