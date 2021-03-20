from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    name = 'Hari Sadu'
    location='@classroom'
    return render_template('index.html',
                           name=name,
                           location=location
                           )


