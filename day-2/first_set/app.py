from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return '''
<h1>Welcome to Flask<a class="headerlink" href="#welcome-to-flask" title="Permalink to this headline"></a></h1>

<a href="https://palletsprojects.com/p/flask/"><img alt="Flask: web development, one drop at a time" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" /></a>

<p>Welcome to Flask’s documentation. Get started with <a href="installation/#installation"><span class="std std-ref">Installation</span></a>

and then get an overview with the <a href="quickstart/#quickstart"><span >Quickstart</span></a>. There is also a
more detailed <a href="tutorial/#tutorial"><span>Tutorial</span></a> that shows how to create a small but
complete application with Flask. Common patterns are described in the
<a href="patterns/#patterns"><span >Patterns for Flask</span></a> section. The rest of the docs describe each component of
Flask in detail, with a full reference in the <a href="api/#api"><span>API</span></a> section.</p>


'''
