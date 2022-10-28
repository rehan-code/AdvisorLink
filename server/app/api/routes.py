from app import app
import json

# Example
@app.route('/')
def ding():
    return json.dumps({'message': 'Ding!'})

@app.route('/course/search')
def search():
    return json.dumps({'message': 'Search!'})


