from flask import Flask, request, jsonify, make_response, has_request_context
from flask import render_template
from flask_caching import Cache
from covid import Covid
from contextlib import closing
import requests
from requests.exceptions import HTTPError
from flask.logging import default_handler
from flask_caching import Cache

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "simple", # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 3000
}

def create_app(): 
	app = Flask(__name__)
	# set up caching config
	app.config.from_mapping(config)
	cache = Cache(app)

	@app.route("/state", methods=["GET"])
	def get_states_data():
		try:
			response = requests.get("https://api.covid19india.org/data.json")
			return response.json()
		except HTTPError as http_err:
			return jsonify(message='Error getting States Covid Data, CovidTracking.com API error', status=500),500
		except Exception as err:
			return jsonify(message='Error getting States Covid Data, CovidTracking.com API error', status=500),500

	@app.route("/statedistrict", methods=["GET"])
	def get_states_district_data():
    		try:
        		response = requests.get("https://api.covid19india.org/state_district_wise.json")
       			return response.text
    		except HTTPError as http_err:
        		return jsonify(message='Error getting State and District Level Covid Data, https://disease.sh API error', status=500),500
    		except Exception as err:
        		return jsonify(message='Error getting State and District Level Covid Data, https://disease.sh API error', status=500),500

	@app.route("/", methods=["GET"])
	def flask_is_up():
		return render_template("index.html")
	return app
