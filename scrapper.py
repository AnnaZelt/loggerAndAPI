import requests
from bs4 import BeautifulSoup
import os

def clean():
    os.system('cls')

URL = "https://www.ynet.co.il/home/0,7340,L-8,00.html"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
with open('scrapper_result.txt', 'w') as f:
    f.write(f"{soup.prettify()}")
# print(soup.prettify())