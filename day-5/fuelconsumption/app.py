import pickle
import numpy as np
import sklearn
from flask import Flask, render_template, request


def create_app():
	app = Flask(__name__)
	model = pickle.load(open('model.pkl', 'rb')) 

	@app.route('/')
	def index():
		return render_template('index.html',) 

	@app.route('/predict', methods=['POST'])
	def predict():
		 feature_array = []
		 for x in request.form.keys():
			 feature_array.append(float(request.form[x]))
		 final_features = [np.array(feature_array)]
		 prediction = model.predict(final_features)
		 prediction = round(prediction[0], 2) 
		 return render_template(
			 'prediction.html',
			 prediction=prediction
		 )
	return app


	
	
