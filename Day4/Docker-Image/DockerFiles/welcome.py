from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "<h1>Hii Welcome to My Web Site</h1>"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)