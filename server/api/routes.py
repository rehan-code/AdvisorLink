from app import app, searchUtil
from flask import request
import json

# Example
@app.route('/api')
def ding():
    return json.dumps({'message': 'Ding!'})

# Get all the sections
@app.route('/api/sections', methods = ['GET'])
def all():
    sections = searchUtil.all()
    searchResultJson = []
    for section in sections:
        searchResultJson.append(section.toJson())

    return json.dumps({'sections' : searchResultJson})

# Search courses by criteria
@app.route('/api/sections/search', methods = ['GET'])
def search():
    sections = searchUtil.search(**request.json.get('query'))
    searchResultJson = []
    for section in sections:
        searchResultJson.append(section.toJson())

    return json.dumps({'sections' : searchResultJson})
