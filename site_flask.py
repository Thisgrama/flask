from flask import Flask, render_template, request
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)

# https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL

@app.route('/')
def index():
    url_moedas = "https://economia.awesomeapi.com.br/xml/available/uniq"
    url_bid = "https://economia.awesomeapi.com.br/last/USD-BRL"
    moedas_request = requests.get(url_moedas)
    bid_request = requests.get(url_bid)

    bid_response = bid_request.json()["USDBRL"]["bid"]
    tree = ET.fromstring(moedas_request.content)
    return render_template('index.html', tree=tree, bid_response=bid_response)

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/receive-value", methods=["POST"])
def receive_value():
    value = request.form["value"]
    # print(value)
    # fazer algo com o value
    return "Value received" + value