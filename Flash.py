from flask import Flask, jsonify, request
import csv

with open('movies.csv') as f:
    reader = csv.reader(f)
    data = list(reader) 
    allmovies = data[1:]

liked_movies = []
not_liked_movies = []
did_not_watch = []

app = Flask(__name__)

@app.route('./get-movie')
def get_movie():
    return jsonify({
        'data':allmovies[0]
        'status':success
    })

@app.route('./liked-movie',methods=['POST'])
def liked_movies():
    movie=allmovies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        'status':success
    })

@app.route('./not_liked_movies',methods=['POST'])
def not_liked_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    not_liked_movies.append(movie)
    return jsonify({
        'status':success
    })

@app.route('./did_not_watch', methods = [POST])
def did_not_watch():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    did_not_watch.append(movie)
    return jsonify({
        'status':success
    })