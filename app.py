from cProfile import run
from curses import flash
from unicodedata import name
from flask import Flask, request, escape

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'world')
    return f'Hello, {escape(name)}!'

""" if __name__ == '__main__':
    pass """