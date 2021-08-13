from logging import debug
from flask import Flask,request,jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'hellth ok'

@app.route('/pre',methods=['POST'])
def postInput():
    insertValue = request.get_json()
    x1 = insertValue['speal']
    input = [x1]
    print (input)
    return jsonify({'return':'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000,debug = True)