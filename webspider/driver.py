from flask import Flask
from selenium import webdriver
app = Flask(__name__)

@app.route("/")
def hello():
    return 'Hello World'


if __name__ == '__main__':
    app.run()
