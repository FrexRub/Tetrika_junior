import pytest

from task3.solution import create_list_interval, summ_times, appearance

intervals = {
    "lesson": [1594663200, 1594666800],
    "pupil": [
        1594663340,
        1594663389,
        1594663390,
        1594663395,
        1594663396,
        1594666472,
    ],
    "tutor": [1594663290, 1594663430, 1594663443, 1594666473],
}


@pytest.mark.parametrize(
    "list_times,list_lesson_tutor,expected",
    [
        ([10, 20, 30, 40], [5, 50], [10, 20, 30, 40]),
        ([5, 15, 25, 35], [10, 30], [10, 15, 25, 30]),
        ([5, 9, 20, 25], [10, 15], []),
    ],
)
def test_create_list_interval(
    list_times: list[int], list_lesson_tutor: list[int], expected: list[int]
):
    result: list[int] = create_list_interval(list_times, list_lesson_tutor)
    assert result == expected


@pytest.mark.parametrize(
    "teme_list, result",
    [([10, 20], 10), ([10, 20, 30, 40], 20), ([], 0)],
)
def test_summ_times(teme_list, result):
    assert summ_times(teme_list) == result


def test_appearance():
    test_answer = appearance(intervals)
    assert test_answer == 3117
