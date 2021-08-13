from flask import Flask
from flask_cors import CORS
import pymongo
from bson.json_util import dumps

client = pymongo.MongoClient("mongodb+srv://root:root123@mycluster.bqv3q.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.website
collection = db.members


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'hellth ok'

@app.route('/pre',methods=['GET'])
def postInput():
    users = collection.find()
    resp = dumps(users)
   
    
    print (resp)
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000,debug = False)