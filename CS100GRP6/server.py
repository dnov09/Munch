# Setting Up Flask
from flask import Flask
from flask import render_template
from flask import jsonify
import os
server = Flask(__name__)

# Importing Other Modules
import requests

# Importing Custom Modules
from app import main

# @server.route('/hello')
# def hello():
#     return 'Hello World!'

# Serving HTML Pages/Templates

@server.route('/')
def home():
    return render_template('index.html', name='Visitor')
    
@server.route('/name/<name>')
def name(name=None):
    return render_template('index.html', name=name)
    
@server.route('/menue')
def menu():
    return render_template('menue.html')
    
@server.route('/requests')
def request():
    return render_template('request.html')
    
@server.route('/caroucel')
def caroucel():
    return render_template('C.html')
    
@server.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# Responding to Requests with Data

@server.route('/reflect/<name>')
def reflect(name=None):
    r = {'name': name}
    return jsonify(r)
    
# @server.route('/weather')
# def weather():
#     w = main.get_weather()
#     return jsonify(w)
    
# @server.route('/location_image/<search>')
# def location_image(search):
#     geo_url = "https://maps.googleapis.com/maps/api/geocode/json"
#     geo_query = {
#         "address": search
#     }
#     geo_res = requests.request("GET", geo_url, params=geo_query);
#     geo_data = geo_res.json();
#     loc = geo_data['results'][0]['geometry']['location'];
#     url = "https://maps.googleapis.com/maps/api/streetview"
#     querystring = {
#         "size": "600x600",
#         "location": str(loc['lat']) + "," + str(loc['lng']),
#         "heading": "90",
#         "pitch": "0"
#     }
#     response = requests.request("GET", url, params=querystring)
#     return response.url;
    
server.run(host=os.getenv('IP','0.0.0.0'),port=int(os.getenv('PORT',8081)))