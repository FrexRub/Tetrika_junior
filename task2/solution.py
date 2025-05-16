import requests

from bs4 import BeautifulSoup

URL_SITE = "https://ru.wikipedia.org"
URL_START = "/wiki/Категория:Животные_по_алфавиту"


def get_data_animals(url: str) -> tuple[list[str], list[str], str]:
    """
    Парсинг данных с сайта
    :param url: str
        адрес сайта
    :return: tuple[list[str], list[str], str]
        возвращает список наименований животных со страницы, список начальных букв, адрес следующей страницы
    """
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
        letter.text for item in data_category_group for letter in item.find_all("h3")
    ]

    return data_animals, list_letters, url_next_page[0]


def get_counts_letters(char: str, list_str: list[str]) -> tuple[int, int]:
    """
    Парсинг данных с сайта
    :param char: str
        начальная буква наименования животного
    :param list_str: list[str]
        список животных с разными начальными буквами
    :return: tuple[int, int]
        количество животных с указанной буквой, количество остальных
    """
    new_list: list[str] = [item for item in list_str if item.startswith(char)]
    return len(new_list), len(list_str) - len(new_list)


if __name__ == "__main__":

    dict_letters: dict[str, int] = dict()

    list_animals, letters, url_next = get_data_animals(URL_SITE + URL_START)
    current_letters: str = letters[-1]
    dict_letters[current_letters] = len(list_animals)

    while "A" not in letters:
        list_animals, letters, url_next = get_data_animals(URL_SITE + url_next)
        if letters[-1] != current_letters:
            count_current_letters, count_next_letters = get_counts_letters(
                current_letters, list_animals
            )

            dict_letters[current_letters] += count_current_letters
            print(f"Проведен расчет для животных на букву: {current_letters}")
            current_letters = letters[-1]
            dict_letters[current_letters] = count_next_letters
        else:
            dict_letters[current_letters] += len(list_animals)

    del dict_letters["A"]
    print(dict_letters)

    with open("beasts.csv", "w", encoding="utf-8") as file:
        for letter, number in dict_letters.items():
            file.write(f"{letter},{number}\n")
