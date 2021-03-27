#Demonstrate MS Excel Program Opening Stuff
from flask import Flask, make_response, render_template
import pandas as pd

# Create Flask's `app` object
app = Flask(__name__)

@app.route("/")
def index():
	 return render_template('index.html',)

	

@app.route("/download")
def download():
	details = { 
		'Name' : ['Ankit', 'Aishwarya', 'Shaurya', 'Shivangi'], 
		'Age' : [23, 21, 22, 21],
		 'University' : ['BHU', 'JNU', 'DU', 'BHU'], 
		} 
	df = pd.DataFrame(details)
	resp = make_response(df.to_csv())
	resp.headers["Content-Disposition"] = "attachment; filename=my_csvfile.csv"
	resp.headers["Content-Type"] = "text/csv"
	return resp


