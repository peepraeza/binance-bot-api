import requests
from decouple import config

url = config('LINE_URL')
token = config('LINE_API_Key')


def sendLineNotification(side, symbol):
    headers = {'content-type': 'application/x-www-form-urlencoded', 'Authorization': 'Bearer ' + token}

    msg = "{} {} Alert\n".format(symbol, side)
    r = requests.post(url, headers=headers, data={'message': msg})
