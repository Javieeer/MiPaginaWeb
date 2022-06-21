from flask import Flask, render_template, request, escape

app = Flask(__name__)

@app.route('https://javieeer.github.io/MiPaginaWeb/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)