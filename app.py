from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/')
def homepage():
    
    return jsonify( { 'tasks': "hello homePage" } )


@app.route('/getUser')
def getUser():
    
    return jsonify( {
    "username": "admin",
    "email": "admin@localhost",
    "id": 42
} )

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

