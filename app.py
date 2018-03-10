from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/')
def homepage():
    
    return jsonify( { 'tasks': "hello homePage" } )


@app.route('/getUser')
def getUser():

    response = jsonify( {
    "username": "sarvesh",
    "email": "sarvesh.y305@gmail.com",
    "id": "Sarvesh19"
    } 
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    )

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

