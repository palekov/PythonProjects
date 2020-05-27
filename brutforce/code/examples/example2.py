import requests

sites = ['https://google.com/', 'https://ya.ru/', 'https://yahoo.com/']
N = 100

for site in sites:
    for i in range(N):
        response = requests.get(site)
        print(i, site, response.status_code)
