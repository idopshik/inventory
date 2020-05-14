from flask import Flask

app = Flask(__name__)

@app.route('/')
def example():
    return '<h1> Hello Flask, there is a lot to go! </h1>'



