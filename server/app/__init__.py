from flask import Flask, request
import json
from app.library.course_search import SearchUtil

searchUtil = SearchUtil()

app = Flask(__name__)

from app import api

@app.errorhandler(404)
def not_found(error=None):
    return {'status': 404, 'message': 'Not Found: ' + request.url}, 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)