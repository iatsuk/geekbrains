"""
Изучить список открытых API.
Найти среди них любое, требующее авторизацию (любого типа).
Выполнить запросы к нему, пройдя авторизацию.
Ответ сервера записать в файл.
"""
import os

import requests

# prepare
# see: https://www.programmableweb.com/api/chess-pastebin-rest-api
endpoint = 'http://www.chesspastebin.com/api/add/'
params = {
    'apikey': os.getenv('apikey', ''),
    'pgn': open('example.pgn').read(),
    'sandbox': 'true',
}

# post data
response = requests.get(endpoint, params=params)

# persist result
if response.text.isdigit():
    pgn_id = response.text
    pgn_url = f'http://www.chesspastebin.com/?p={pgn_id}'
    open(f'posted_pgn.txt', 'a').write(f'{pgn_url}\n')
else:
    raise Exception(f'Server response: {response.text}')
