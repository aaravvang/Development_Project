from flask import Flask, request



app = Flask(__name__)


@app.route("/")
def home():
    return "This is the homepage"


@app.route("/calculation", methods=['POST'])
def discount():
    age=float(request.form.get("age"))
    isStudent = bool(request.form.get("isStudent"))
    
    if(age<5 or age>60):
        return "50 percent"
    elif(age<=25 and isStudent):
        return "25 percent discount"
    else:
        return "No discount"

@app.route("/healthcheck")
def healthcheck():
     return "The services are fine, no maintenance needed."


if __name__ == "__main__":
    app.run(debug=True)

