from typing import Union
import re


def get_filter(data: Union[list, map, filter, set], value: str) -> filter:
    """Применение фильтра"""
    check_type(data)
    if not isinstance(value, str):
        raise TypeError
    return filter(lambda line: value in line.lower(), data)


def get_map(data: Union[list, map, filter, set], value: Union[str, int]) -> map:
    """Применение столбцов"""
    check_type(data)
    try:
        value = int(value)
    except Exception:
        raise TypeError
    return map(lambda line: parse_string(line)[value - 1] + '\n', data)


def get_unique(data: Union[list, map, filter, set], value=None) -> set:
    """Применение уникальности"""
    check_type(data)
    return set(data)


def get_sort(data: Union[list, map, filter, set], value: str) -> list:
    """Применение сортировки по алфавиту"""
    check_type(data)
    if value not in ['asc', 'decs']:
        raise ValueError
    return sorted(data, reverse=(value == 'desc'))


def get_limit(data: Union[list, map, filter, set], value: Union[str, int]) -> list:
    """Применение ограничения"""
    check_type(data)
    print(type(data))
    try:
        value = int(value)
    except Exception:
        raise TypeError
    return list(data)[:value]


def get_regexp(data: list, value: str) -> list:
    """Применение регулярного выражения"""
    check_type(data)
    return list(filter(lambda rec: re.search(value, rec), data))


def parse_string(string: str) -> list:
    """Парсинг данных из запроса"""
    return string.split()


def check_type(data):
    """Проверка типа данных"""
    if not isinstance(data, (list, map, filter, set)):
        raise TypeError
