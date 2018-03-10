from flask import Flask, request, jsonify
from datetime import datetime
from flask_restful import Resource, Api
from json import dumps

app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)

class Employees(Resource):
    def get(self):

        return {
    "employees": [
        1, 
        2, 
        3, 
        4, 
        5, 
        6, 
        7, 
        8
    ]
} # Fetches first column that is Employee ID

api.add_resource(Employees, '/employees') # Route_1

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

