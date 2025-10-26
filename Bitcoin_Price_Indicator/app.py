from flask import Flask, request
import requests
import sys

app = Flask(__name__)


apiKey = "9d2d550d0c75a441c611c1b0dd8d8d2e2a366c0a176651b122addec8a4a4a547"

url = f"rest.coincap.io/v3/assets/bitcoin?apiKey={apiKey}"

response = requests.get(url)

def get_bitcoin_price():
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("You cannot repeat a bitcoin price!")

app.route('/bitcoin', methods=['POST'])
def bitcoinPrice():
    number = float(request.form.get('number'))  
    bitcoin_price = get_bitcoin_price()
    total_cost = number * bitcoin_price
    print(f"${total_cost:,.4f}")
    



    


print(response)
