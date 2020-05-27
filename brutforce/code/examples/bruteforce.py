# 0123456789ABCDEF
# 0123456789qwertyuiopasdfghjklzxcvbnm!@#$%^&*(

# 1 - 1
# 2 - 2
# ...
# 9 - 9
# 10 - A
# 11 - B
# 12 - C
# ...
# 15 - F
# 16 - 10
# ...
# 16 ^ 2 - 100
# 16^2 + 1 - 101
# 5827 - 16C3
# ...
# ??? - CA1DF
import requests


alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
base = len(alphabet)

i = 0
length = 0

while True:
    # i: 10 -> base

    password = ''
    temp = i
    while temp != 0:
        rest = temp % base
        temp = temp // base
        password = alphabet[rest] + password

    # while len(password) < length:
    #     password = '0' + password
    password = alphabet[0] * (length - len(password)) + password

    print(length, i, password)
    response = requests.post('http://127.0.0.1:4000/auth',
                             json={'login': 'cat', 'password': password})
    if response.status_code == 200:
        print('Success!')
        break

    if password == alphabet[-1] * length:
        length += 1
        i = 0
    else:
        i += 1
