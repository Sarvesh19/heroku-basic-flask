from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def homepage():
    
    return jsonify( { 'tasks': "hello homePage" } )


@app.route('/getUser', methods=['POST'])
@cross_origin()
def getUser():
userName = request.form.get('userName')
password = request.form.get('password')

if userName == 'sarvesh' and password == 'sarvesh123': 
    
     return jsonify( {
    "username": "sarvesh",
    "email": "sarvesh.y305@gmail.com",
    "id": "Sarvesh19"
    } 
    )
  else return 'Not Authorize Person'  
    

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

