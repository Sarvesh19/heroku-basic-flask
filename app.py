from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
@cross_origin()
def homepage():
    
    return jsonify( { 'tasks': "hello homePage" } )


@app.route('/getUser')
@cross_origin()
def getUser():

     return jsonify( {
    "username": "sarvesh",
    "email": "sarvesh.y305@gmail.com",
    "id": "Sarvesh19"
    } 
    )

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

