import requests
import pytest

from task2.solution import get_data_animals, URL_SITE, URL_START


def test_get_site():
    result = requests.get(URL_SITE + URL_START)
    assert result.status_code == 200


@pytest.mark.parametrize("url_1, url_2", [(URL_SITE, URL_START)])
def test_get_data_animals(url_1, url_2):
    list_animals, letters, url_next = get_data_animals(url_1 + url_2)
    assert "А" in letters
    assert "Аардоникс" in list_animals
