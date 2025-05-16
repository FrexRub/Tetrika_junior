from functools import wraps
from typing import Callable


def strict(func: Callable):
    @wraps(func)
    def wrapped(*args, **kwargs):
        annotations = tuple(func.__annotations__.values())
        if args:
            for i in range(len(args)):
                if not isinstance(args[i], annotations[i]):
                    raise TypeError("Неверный тип данных")
        if kwargs:
            for key, val in kwargs.items():
                if not isinstance(val, func.__annotations__[key]):
                    raise TypeError("Неверный тип данных")
        return func(*args, **kwargs)

    return wrapped


@strict
def sum_two(a: int, b: int) -> int:
    return a + b

@strict
def sum_two_float(a: float, b: float) -> float:
    return a + b


@strict
def concat_strings(s1: str, s2: str) -> str:
    return s1 + s2


@strict
def check_bool(a: bool, b: bool) -> bool:
    return a is b
