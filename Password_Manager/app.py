from flask import Flask, request


app = Flask(__name__)


@app.route("/", methods=['GET'])
def encrypt():
    password= request.args.get("password")
    key=int(request.args.get("key"))

    encryption = ""
    counter = 1
    for i in password:
        value = ord(i)
        if(counter%2!=0):
            value+=key
        else:
            value-=key
        encryption+=chr(value)
        counter+=1
    return encryption

if __name__ == "__main__":
    app.run(debug=True)

        
        
