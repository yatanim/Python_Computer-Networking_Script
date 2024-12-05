import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text,'html.parser')

    links = soup.find_all(['h1', 'p','a'])

    print(f"Links found on {url}:")

    for link in links:
        print(f"Text:{link.get_text()}")
        print(f"title:{link.get('title')}")
        print(f"url:{link.get('href')}")
        print("-"*50)
else:
    print(f"failed to restrieve content from {url}")

