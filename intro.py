from flask import Flask


app = Flask("Hello")

@app.route("/")
def home():
    return "Hello World"


@app.route("/donuts")
def donuts():
    return "I love donuts"

if __name__ == "__main__":
    app.run(debug=True)

