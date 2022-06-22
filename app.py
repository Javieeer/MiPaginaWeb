from unicodedata import name
from flask import Flask, render_template, request, escape

app = Flask(__name__)

@app.route('https://javieeer.github.io/MiPaginaWeb/')
def index():
    return render_template('index.html')