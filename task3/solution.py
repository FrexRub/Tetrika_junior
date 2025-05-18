tests = [
    {
        "intervals": {
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
        },
        "answer": 3117,
    },
    {
        "intervals": {
            "lesson": [1594692000, 1594695600],
            "pupil": [1594692033, 1594696347],
            "tutor": [1594692017, 1594692066, 1594692068, 1594696341],
        },
        "answer": 3565,
    },
    {
        "intervals": {
            "lesson": [1594702800, 1594706400],
            "pupil": [
                1594702789,
                1594704500,
                1594702807,
                1594704542,
                1594704512,
                1594704513,
                1594704564,
                1594705150,
                1594704581,
                1594704582,
                1594704734,
                1594705009,
                1594705095,
                1594705096,
                1594705106,
                1594706480,
                1594705158,
                1594705773,
                1594705849,
                1594706480,
                1594706500,
                1594706875,
                1594706502,
                1594706503,
                1594706524,
                1594706524,
                1594706579,
                1594706641,
            ],
            "tutor": [
                1594700035,
                1594700364,
                1594702749,
                1594705148,
                1594705149,
                1594706463,
            ],
        },
        "answer": 3577,
    },
]


def create_list_interval(
    list_times: list[int], list_lesson_tutor: list[int]
) -> list[int]:
    """
    Создаем пересекающихся временных интервалов
    :param list_times: list[int]
        входной список (pupil или tutor)
    :param list_lesson_tutor: list[int]
        входной список (lesson или tutor)
    :return: list[int]
        возвращает список пересекающихся временных интервалов
    """
    list_intervals: list[int] = list()
    for i_num in range(0, len(list_times), 2):
        start_interval: int = max(list_times[i_num], list_lesson_tutor[0])
        end_interval: int = min(list_times[i_num + 1], list_lesson_tutor[1])
        if start_interval < end_interval:
            list_intervals.extend([start_interval, end_interval])
    return list_intervals


def summ_times(intervals_times: list[int]) -> int:
    """
    Расчет суммы временных интервалов
    :param intervals_times: list[int]
        входной список (pupil или tutor)
    :return: int
        возвращает сумму временных интервалов
    """
    sum_times: int = 0
    for i_num in range(0, len(intervals_times), 2):
        sum_times += intervals_times[i_num + 1] - intervals_times[i_num]
    return sum_times


def appearance(intervals: dict[str, list[int]]) -> int:
    """
    Расчет суммы пересекающихся временных интервалов
    :param intervals: dict[str, list[int]]
        словарь временных интервалов с ключами: lesson - уроки, pupil - учащиеся, tutor - преподаватели
    :return: int
        возвращает сумму временных интервалов
    """
    list_intervals_pupil: list[int] = create_list_interval(
        intervals["pupil"], intervals["lesson"]
    )

    list_intervals_tutor: list[int] = create_list_interval(
        intervals["tutor"], intervals["lesson"]
    )

    list_intervals_all: list[int] = list()
    for i_num in range(0, len(list_intervals_tutor), 2):
        list_intervals: list[int] = create_list_interval(
            list_intervals_pupil,
            [list_intervals_tutor[i_num], list_intervals_tutor[i_num + 1]],
        )
        list_intervals_all.extend(list_intervals)

    return summ_times(list_intervals_all)


if __name__ == "__main__":
    for i, test in enumerate(tests):
        test_answer: int = appearance(test["intervals"])  # type: ignore[arg-type]
        assert (
            test_answer == test["answer"]
        ), f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
