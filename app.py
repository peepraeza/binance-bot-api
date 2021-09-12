from flask import Flask, request
from services.binanceBot import *

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/webhook", methods=['POST'])
def signalWebHook():
    req = request.json
    resource = req['resource']
    if resource != 'tradingView':
        return {
            "code": "error",
            "message": "sorry can't not execute order"
        }
    side = req['side']
    symbol = req['symbol']
    order_resp = order(side, symbol)
    if order_resp:
        return {
            "code": "success",
            "message": "order executed"
        }
    else:
        return {
            "code": "error",
            "message": "can't fetch balance from binance"
        }


@app.route("/check-balance", methods=['POST'])
def balance():
    req = request.json
    asset = req['asset']
    balance = checkBalance(asset)
    if (balance):
        return {
            "code": "success",
            "data": {
                "amount": balance,
                "asset": asset
            }

        }
    else:
        return {
            "code": "error",
            "message": "can't fetch balance from binance"
        }


if __name__ == "__main__":
    app.run(debug=True)
