import os

import requests
import pytest

from task2.solution import (
    get_data_animals,
    URL_SITE,
    URL_START,
    get_counts_letters,
    write_data_in_file,
)


def test_get_site():
    result = requests.get(URL_SITE + URL_START)
    assert result.status_code == 200


@pytest.mark.parametrize(
    "url_1, url_2, i_chr, name", [(URL_SITE, URL_START, "А", "Аардоникс")]
)
def test_get_data_animals(url_1, url_2, i_chr, name):
    list_animals, letters, url_next = get_data_animals(url_1 + url_2)
    assert i_chr in letters
    assert name in list_animals


@pytest.mark.parametrize(
    "i_chr, list_name, count",
    [
        ("А", ["Аардоникс", "Абелизавриды"], 2),
        ("В", ["Абингдонская слоновая черепаха", "Веероусы"], 1),
    ],
)
def test_get_counts_letters(i_chr, list_name, count):
    assert get_counts_letters(i_chr, list_name) == count


def test_write_data_in_file(tmp_path):
    test_data = {"А": 642, "Б": 412, "В": 100}
    test_file = tmp_path / "beasts.csv"

    write_data_in_file(test_data)

    assert os.path.exists("beasts.csv")

    with open("beasts.csv", "r", encoding="utf-8") as file:
        lines = file.readlines()

    assert len(lines) == len(test_data)

    for line in lines:
        letter, number = line.strip().split(",")
        assert letter in test_data
        assert int(number) == test_data[letter]

    if os.path.exists("beasts.csv"):
        os.remove("beasts.csv")
