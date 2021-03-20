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


@app.route('/square/<number>')
def handle_square(number):
    error = None
    sq = None
    try:
        sq = int(number) * int(number)
    except Exception as e:
        print ("Error: ", e)
        error = 1

    return render_template('square.html',
                           number=number,
                           square=sq,
                           error = error
                           )

