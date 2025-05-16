import pytest

from task1.solution import sum_two, sum_two_float, concat_strings, check_bool


@pytest.mark.parametrize("a, b, result", [(1, 2, 3), (2, 2, 4), (4, -4, 0)])
def test_sum_two_correct_arg(a, b, result):
    assert sum_two(a, b) == result


@pytest.mark.parametrize("a, b", [(1, "2"), ("2", 2), ("4", "-4"), (4, 2.3), (1.2, 3), (2.2, 2.3)])
def test_sum_two_incorrect_arg(a, b):
    with pytest.raises(TypeError, match="Неверный тип данных"):
        sum_two(a, b)


@pytest.mark.parametrize("a, b, result", [(1.1, 2.0, 3.1), (2.2, 2.2, 4.4), (4.0, 3.1, 7.1)])
def test_sum_two_float_correct_arg(a, b, result):
    assert sum_two_float(a, b) == result


@pytest.mark.parametrize("a, b", [(1, "2"), ("2", 2), ("4", "-4"), (4, 2.3), (1.2, 3), (2, 2)])
def test_sum_two_float_incorrect_arg(a, b):
    with pytest.raises(TypeError, match="Неверный тип данных"):
        sum_two_float(a, b)


@pytest.mark.parametrize("a, b, result", [("1", "2", "12"), ("Hello ", "world", "Hello world")])
def test_concat_strings_correct_arg(a, b, result):
    assert concat_strings(a, b) == result


@pytest.mark.parametrize("a, b", [("1", 2), (1, "2"), (1.2, "world"), ("world", 1), (7, 1)])
def test_concat_strings_incorrect_arg(a, b):
    with pytest.raises(TypeError, match="Неверный тип данных"):
        concat_strings(a, b)


@pytest.mark.parametrize("a, b, result", [(True, True, True), (False, False, True), (True, False, False), (False, True, False)])
def test_check_bool_correct_arg(a, b, result):
    assert check_bool(a, b) == result


@pytest.mark.parametrize("a, b", [(True, 2), (1, False), (1.2, True), (False, 1.1), ("Hello", True), (True, "Hello")])
def test_check_bool_incorrect_arg(a, b):
    with pytest.raises(TypeError, match="Неверный тип данных"):
        check_bool(a, b)
