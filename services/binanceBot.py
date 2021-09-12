import ccxt
from decouple import config
from services.lineNotify import *
from binance.client import Client
from binance.enums import *

api_key = config('Binance_API_Key')
api_secret = config('Binance_API_Secret')

usdt_amount = config('Limit_Buy_Per_Asset')

client = Client(api_key, api_secret)


def order(side, symbol, order_type=ORDER_TYPE_MARKET):
    try:
        asset = symbol.replace("USDT", "")
        side = side.upper()
        if side == "SELL":
            quantity = checkBalance(asset)
        else:
            quantity = calculateQuantity(usdt_amount, symbol)
        # order = client.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
        # sendLineNotification(side, symbol)
        print(f"sending order {order_type} - {side} {quantity} {symbol}")
        order = {'test': 1}
        print(order)
    except Exception as e:
        print("an exception occurred - {}".format(e))
        return False
    return order


def checkBalance(asset):
    try:
        balance = client.get_asset_balance(asset)
        amount = balance['free']
    except Exception as e:
        print("an exception occurred - {}".format(e))
        return False
    return amount


def calculateQuantity(usdt_limit, symbol):
    try:
        avg_price = client.get_avg_price(symbol=symbol)
        buy_quantity = float(usdt_limit) / float(avg_price['price'])
        print("{}: price is {}".format(symbol, avg_price['price']))
        print('you can buy amount {}'.format(buy_quantity))
        return buy_quantity
    except Exception as e:
        print("an exception occurred - {}".format(e))
        return False
