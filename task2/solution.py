import requests

from bs4 import BeautifulSoup

url_site = "https://ru.wikipedia.org"
url_start = "/wiki/Категория:Животные_по_алфавиту"


def get_data_animals(url: str) -> tuple[list[str], list[str], str]:
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    target_div = soup.find_all("div", id="mw-pages")
    url_next_page = [
        a["href"]
        for item in target_div
        for a in item.find_all("a")
        if a.text == "Следующая страница"
    ]

    data_category_group = soup.find_all("div", class_="mw-category-group")
    page_data = [
        item.find_all("li") for item in data_category_group if item.find("div") is None
    ]
    data_animals = [li.find("a").text for li_list in page_data for li in li_list]
    list_letters = [
        letter.text
        for item in data_category_group
        for letter in item.find_all("h3")
        if item.find("div", class_="mw-content-ltr")
    ]

    print(list_letters)

    return data_animals, list_letters, url_next_page[0]


if __name__ == "__main__":

    list_animals, letters, url_next = get_data_animals(url_site + url_start)
    print(list_animals)

    while "Б" not in letters:
        list_animals, letters, url_next = get_data_animals(url_site + url_next)
        print(list_animals)
