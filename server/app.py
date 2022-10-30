from flask import Flask, request
import json
import pandas as pd

courseList = pd.read_excel('prototyping/course_schedule_spreadsheet.xlsm', sheet_name='course list')
# accessing column: courselist['column name']
# accessing: courselist.loc[start:stop:step]

# print(courseList)

app = Flask(__name__)

@app.route('/')
def ding():
    return json.dumps({'message': 'Ding!'})

@app.errorhandler(404)
def not_found(error=None):
    return {'status': 404, 'message': 'Not Found: ' + request.url}, 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
