from flask import Flask, request

app = Flask(__name__)

@app.route("/hello", methods=['GET'])
def uniqueName():
    name=request.args.get("q")
    return ("Hello "+ name)

@app.route("/")
def home():
    return "This is the home page"


if __name__ == "__main__":
    app.run(debug=True)
