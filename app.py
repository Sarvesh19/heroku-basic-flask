from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'hello'
)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

