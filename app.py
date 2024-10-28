from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, this is CICD pipeline"

@app.route("/about")
def about():
    return "This is about page"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
