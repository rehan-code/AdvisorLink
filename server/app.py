from flask import Flask, request
import json

app = Flask(__name__, static_url_path='')

@app.route('/ding')
def ding():
    return json.dumps({'message': 'Ding!'})

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.errorhandler(404)
def not_found(error=None):
    return {'status': 404, 'message': 'Not Found: ' + request.url}, 404

if __name__ == '__main__':
    app.run(debug = True)
