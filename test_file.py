from collections.abc import Iterable

list = [1, 2, 3, 4]


def replace_first(items: list) -> Iterable:
    list.pop()
    return list

print(list)


