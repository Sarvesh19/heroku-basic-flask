from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def homepage():
    #the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return jsonify(
        username='sarvesh',
        email=g.'dwdwd@ce.com',
        id='14'
    )
)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

