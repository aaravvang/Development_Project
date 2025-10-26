from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("login.html")

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    password = request.form['password']

    print(name)
    print(password)

    if((name == "admin") and (password == "admin")) :
        return f"Hello, {name}! Login successful!"
    else:
        return "You aren't an admnistrator, please try again later."
    

if __name__ == "__main__":
    app.run(debug=True)