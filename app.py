from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type: application/json'

@app.route('/')
@cross_origin()
def homepage():
    
    return jsonify( { 'tasks': "hello homePage" } )


@app.route('/getUser', methods=["GET","POST"])
@cross_origin()
def getUser():
 
if request.method == "POST":
    
    attempted_username = request.form['userName']
     attempted_password = request.form['password']

        if attempted_username == "sarvesh" and attempted_password == "sarvesh123":
    
     return jsonify( {
    "username": "sarvesh",
    "email": "sarvesh.y305@gmail.com",
    "id": "Sarvesh19"
    } 
    )
    else:
        return 'Not Authorize Guy'
    

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

