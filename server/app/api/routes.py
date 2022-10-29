from app import app, searchUtil
from flask import request
import json

# Example
@app.route('/')
def ding():
    return json.dumps({'message': 'Ding!'})

# Get all the sections
@app.route('/sections', methods = ['GET'])
def all():
    sections = searchUtil.all()
    searchResultJson = []
    for section in sections:
        searchResultJson.append(section.toJson())

    return json.dumps({'sections' : searchResultJson})

# Search courses by criteria
@app.route('/sections/search', methods = ['GET'])
def search():
    sections = searchUtil.search(**request.json.get('search_by'))
    searchResultJson = []
    for section in sections:
        searchResultJson.append(section.toJson())

    return json.dumps({'sections' : searchResultJson})


