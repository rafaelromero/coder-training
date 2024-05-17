from flask import Flask, jsonify
from flask import request
from flask_cors import CORS
import csv

app = Flask(__name__)
CORS(app)

@app.route("/movies", methods=["GET", "POST"])
def movies():
    if request.method == "POST":
        movie = request.json
        result = insert_movie()  #??
        return result
    else:
        movies =  get_movies()
        return movies


def insert_movie(name, year, rating):
    with open("data.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow([name, year, rating])
    return {"status": "success"}


def get_movies():
    movies = [] 
    with open('data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            movies.append(row)
    return jsonify({'movies':movies})