from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/')
def homepage():
    
    return jsonify( { 'tasks': "hello homePage" } )


@app.route('/getUser')
def getUser():

     return jsonify( {
    "username": "sarvesh",
    "email": "sarvesh.y305@gmail.com",
    "id": "Sarvesh19"
    } 
    )

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

