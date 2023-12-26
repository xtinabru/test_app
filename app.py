from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Что могу, то и делаю"

if __name__ == '__main__':
    app.run(debug=True)
