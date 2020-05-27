import requests
 
websites = [  
    "https://ya.ru/",
    "https://vk.com/",
    "https://www.ok.ru/",
    "https://www.tut.by/",
    "https://www.facebook.com/"
]
 
request_num = 1
for site in websites:
    for _ in range(100):
        response = requests.get(site)
        print(f"Website: {site}")
        print(f"Status code: {response.status_code}")
        print(f"Number of request: {request_num}\n")
        request_num += 1