from functools import wraps
from typing import Callable


def strict(func: Callable):
    @wraps(func)
    def wrapped(*args, **kwargs):
        print(func.__annotations__)
        annotations = tuple(func.__annotations__.values())
        if args:
            for i in range(len(args)):
                if not isinstance(args[i], annotations[i]):
                    raise TypeError("Не верный тип данных")
        if kwargs:
            for key, val in kwargs.items():
                if not isinstance(val, func.__annotations__[key]):
                    raise TypeError("Неверный тип данных")

        return func(*args, **kwargs)

    return wrapped


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(1, 2))
print(sum_two(1, 2.4))
