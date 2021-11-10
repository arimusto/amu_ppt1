from random import choice
from string import ascii_letters as ltrs
from hashlib import md5
from flask import Flask, send_file

with open("file.txt", "w", encoding = "utf-8") as file:
    random_text = ""
    for _ in range(1024):
        random_text += choice(ltrs)
    file.write(random_text)

app = Flask(__name__)

@app.route("/")
def hello():
    return send_file("./hello.html")
