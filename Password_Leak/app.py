from flask import Flask, render_template, request, redirect, url_for
import itertools

app = Flask(__name__)


passwords = []
_id_gen = itertools.count(1)  

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", passwords=passwords)

@app.route("/add", methods=["POST"])
def add_password():
    value = request.form.get("value", "")
    if value:
        passwords.append({"id": next(_id_gen), "value": value})
    return redirect(url_for("index"))

@app.route("/delete/<int:password_id>", methods=["POST"])
def delete_password(password_id):
    global passwords
    new_list = []
    for p in passwords:
        if p["id"] != password_id:
            new_list.append(p)

    passwords = new_list
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)