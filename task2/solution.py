import requests

from bs4 import BeautifulSoup


def set_dict_url() -> dict[str, str]:
    url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"

    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    all_data = soup.find_all("div", class_="ts-module-Индекс_категории-container")
    all_url = soup.find_all("a", class_="external text")

    urls = {item.text : item["href"] for item in all_url if len(item.text) == 2}
    return urls


if __name__ == "__main__":
    dict_urls = set_dict_url()
    for letter, url_letter in dict_urls.items():
        print(letter, url_letter)



