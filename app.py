from flask import Flask


app = Flask(__name__)

@app.route('/')
def homepage():
    return 'hello world i am flask service from heroku'



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

