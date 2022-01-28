import api
import xlrd
import csv
from datetime import datetime, timedelta
from flask import Flask, render_template
from flask_restful import Api, Resource
import requests
import json

app = Flask(__name__)
api = Api(app)


@app.route('/', methods=['GET'])
def home():
    joke_list = []
    for i in range(10):
        request_joke = requests.get('http://api.icndb.com/jokes/random/')
        data_item = json.loads(request_joke.content)
        joke_list.append(data_item)

    string_list = []
    for i in range(10):
        string_list.append(joke_list[i]['value']['joke'])


    return render_template('index.html', data=string_list)


class Jokes(Resource):
    pass


api.add_resource(Jokes, '/http://localhost:5000/getJokes')

if __name__ == "__main__":
    app.run()
