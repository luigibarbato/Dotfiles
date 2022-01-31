import feedparser
import json
import flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin
from pymongo import MongoClient
app = flask.Flask(__name__)
cors = CORS(app)
app.config["DEBUG"] = True
app.config['CORS_HEADERS'] = 'Content-Type'
# Connect to MongoDB instance running on localhost
client = MongoClient()          
#Use the new datastore datastructure
d = []
articles = []


@app.route('/', methods=['GET'])
@cross_origin()
def home():

    sources = data["IT"]["sources"]
    for feed in sources:
        try:
            d.append(feedparser.parse(str(feed["feedlink"])))
        except:
            print("ops")

    for x in d:
        for e in x.entries:
            if("covid" in e.description):
                article = {}
                article["title"] = e.title
                article["url"] = e.link
                article["published"] = e.published
                if(len(e.enclosures)>0):
                    article["thumb"] = e.enclosures[0].href
                articles.append(article)

    return jsonify(articles)

app.run()
