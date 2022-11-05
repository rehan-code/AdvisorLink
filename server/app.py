from flask import Flask, request
from library.course_search import SearchUtil
import os
from db import db
context = (os.path.join(os.path.dirname(__file__), 'certs/cert.crt'), os.path.join(os.path.dirname(__file__), 'certs/private.key'))

searchUtil = SearchUtil()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:Fall2022CIS3760@localhost:5432/advisorlink'
db.init_app(app)

from api.routes import *

@app.errorhandler(404)
def not_found(error=None):
    return {'status': 404, 'message': 'Not Found: ' + request.url}, 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, ssl_context=context)
