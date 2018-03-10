from flask import Flask


app = Flask(__name__)

@app.route('/')
def homepage():
    
    return {
    "username": "admin",
    "email": "admin@localhost",
    "id": 42
}



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

