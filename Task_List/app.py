# from flask import Flask, request, render_template


# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template("index.html")




# if __name__ == "__main__":
#     app.run(debug=True)



from flask import Flask, render_template, request, redirect, url_for
import itertools

app = Flask(__name__)

# simple in-memory storage
tasks = []
_id_gen = itertools.count(1)  # generates unique incremental IDs

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title", "")
    if title:
        tasks.append({"id": next(_id_gen), "title": title})
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    new_tasks = []
    for t in tasks:
        if t["id"] != task_id:
            new_tasks.append(t)

    tasks = new_tasks

    return redirect(url_for("index"))

if __name__ == "__main__":
    # debug True for development only
    app.run(debug=True, host="127.0.0.1", port=5000)