from flask import Flask, request


app = Flask(__name__)


@app.route("/", methods=['GET'])
def converter():
    temp=float(request.args.get("temp"))
    unit=request.args.get("unit")
    print(unit)
    print(type(unit))

    if(unit=='C'):
        temp =(temp * (9/5))+32
    elif(unit == "F"):
        temp = (temp-32)*(5/9)
    else:
        return "wrong input please try again"
    return str(temp)


if __name__ == "__main__":
    app.run(debug=True)



