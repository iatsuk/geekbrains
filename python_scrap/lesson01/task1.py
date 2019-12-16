"""
Посмотреть документацию к API GitHub.
Разобраться как вывести список репозиториев для конкретного пользователя.
Сохранить JSON-вывод в файле *.json.
"""
import json

import requests

# prepare
# see: https://developer.github.com/v3/
headers = {'Accept': 'application/vnd.github.v3+json',}
endpoint = 'https://api.github.com'
user = 'yatsukav'
user_url = f'/users/{user}/repos'

# get data
response = requests.get(f'{endpoint}{user_url}', headers=headers)

# persist result
if response.ok:
    repos = json.loads(response.text)
    for repo in repos:
        print(f'{repo["name"]} - {repo["description"]}')
        print(f'git clone {repo["ssh_url"]}')
        print()
    with open(f'repos_{user}.json', 'w') as f:
        json.dump(repos, f, indent=4, sort_keys=True)
else:
    raise Exception(f'Server response code: {response.status_code}')
