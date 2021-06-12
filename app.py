from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h3>Hello CI/CD!</h3>"
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
