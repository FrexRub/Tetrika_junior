import logging

import requests
from bs4 import BeautifulSoup, Tag
from bs4.element import ResultSet, PageElement, NavigableString

URL_SITE = "https://ru.wikipedia.org"
URL_START = "/wiki/Категория:Животные_по_алфавиту"

logging.basicConfig(
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
    format="[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s",
)
logger = logging.getLogger(__name__)


def get_data_animals(url: str) -> tuple[list[str], list[str], str]:
    """
    Парсинг данных с сайта
    :param url: str
        адрес сайта
    :return: tuple[list[str], list[str], str]
        возвращает список наименований животных со страницы, список начальных букв, адрес следующей страницы
    """
    page: requests.Response = requests.get(url)
    soup: BeautifulSoup = BeautifulSoup(page.text, "html.parser")

    target_div: ResultSet[PageElement | Tag | NavigableString] = soup.find_all(
        "div", id="mw-pages"
    )

    url_next_page: list[str] = [
        a["href"]
        for item in target_div
        for a in item.find_all("a")  # type: ignore[union-attr]
        if a.text == "Следующая страница"  # type: ignore[union-attr]
    ]

    data_category_group: ResultSet[PageElement | Tag | NavigableString] = soup.find_all(
        "div", class_="mw-category-group"
    )

    page_data: list[ResultSet[Tag]] = [
        item.find_all("li") for item in data_category_group if item.find("div") is None  # type: ignore[union-attr]
    ]

    data_animals: list[str] = [
        li.find("a").text for li_list in page_data for li in li_list  # type: ignore[union-attr]
    ]

    list_letters: list[str] = [
        letter.text for item in data_category_group for letter in item.find_all("h3")  # type: ignore[union-attr]
    ]

    return data_animals, list_letters, url_next_page[0]


def get_counts_letters(char: str, list_str: list[str]) -> int:
    """
    Парсинг данных с сайта
    :param char: str
        начальная буква наименования животного
    :param list_str: list[str]
        список животных с разными начальными буквами
    :return:  int
        количество животных с указанной начальной буквой
    """
    new_list: list[str] = [item for item in list_str if item.startswith(char)]
    return len(new_list)


def write_data_in_file(dict_data: dict[str, int]) -> None:
    """
    Запись данных в файл
    :param dict_data: dict[str, int]
        данные о количестве букв в названиях животных
    :return:  None
    """
    logger.info("Начало записи файла beasts.csv")
    with open("beasts.csv", "w", encoding="utf-8") as file:
        for letter, number in dict_data.items():
            file.write(f"{letter},{number}\n")

    logger.info("Завершение записи файла beasts.csv")


def main() -> None:
    dict_letters: dict[str, int] = dict()

    list_animals, letters, url_next = get_data_animals(URL_SITE + URL_START)
    current_letters: str = letters[-1]
    dict_letters[current_letters] = len(list_animals)

    # пока на странице не появится латинская А
    while "A" not in letters:
        list_animals, letters, url_next = get_data_animals(URL_SITE + url_next)
        if letters[-1] != current_letters:
            count_current_letters = get_counts_letters(current_letters, list_animals)
            dict_letters[current_letters] += count_current_letters
            logger.info(f"Проведен расчет для животных на букву: {current_letters}")
            # если на странице несколько букв
            i_chr = -1
            while current_letters != letters[i_chr]:
                i_chr -= 1

            while i_chr != -1:
                i_chr += 1
                count_current_letters = get_counts_letters(letters[i_chr], list_animals)
                dict_letters[letters[i_chr]] = count_current_letters

            current_letters = letters[-1]
        else:
            dict_letters[current_letters] += len(list_animals)

    del dict_letters["A"]

    write_data_in_file(dict_letters)


if __name__ == "__main__":
    main()
