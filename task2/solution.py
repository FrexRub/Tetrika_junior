import requests

from bs4 import BeautifulSoup

url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

all_data = soup.find_all("div", class_="ts-module-Индекс_категории-container")
all_url = soup.find_all("a", class_="external text")

dict_urls = {item.text : item["href"] for item in all_url if len(item.text) == 2}

for key, val in dict_urls.items():
    print(key, val)


