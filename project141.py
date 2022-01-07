from flask import Flask, jsonify, request
import csv

all_articles = []
with open("class141/articles.csv", encoding = 'utf8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
unliked_articles = []

app = Flask(__name__)

@app.route("/get-article")
def get_article():
    return jsonify({
        "data":all_articles[0],
        "status":"success"
    })

@app.route("/liked-article", methods = ["POST"])
def liked_article():
    global all_articles
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "data":article,
        "status":"success"
    }),201

@app.route("/unliked-article", methods = ["POST"])
def unliked_article():
    global all_articles
    article = all_articles[0]
    all_articles = all_articles[1:]
    unliked_articles.append(article)
    return jsonify({
        "data":article,
        "status":"success"
    }),201

app.run()