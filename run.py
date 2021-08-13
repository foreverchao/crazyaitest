from flask import Flask
from flask_cors import CORS
import pymongo
from bson.json_util import dumps



app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'hellth ok'


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000,debug = False)