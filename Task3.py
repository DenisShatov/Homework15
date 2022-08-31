#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime


def cashe(file):
    def make_log(old_function, ):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)

            with open(file, 'a', encoding="utf-8") as logs_file:
                logs_file.write(f'Дата и время вызова функции: {datetime.now()}, '
                                f'имя функции: {old_function.__name__}, '
                                f'аргументы: {args} {kwargs}, '
                                f'возвращаемое значение: {result}\n')

            return result
        return new_function
    return make_log


@cashe(file='log3.txt')
def flat_generator(lst):
    ex_cursor = 0
    in_cursor = 0

    try:
        while ex_cursor < len(lst):
            iterator = iter(lst[ex_cursor])
            while in_cursor < len(lst[ex_cursor]):
                yield next(iterator)
                in_cursor += 1
            ex_cursor += 1
            in_cursor = 0
    except StopIteration:
        pass


if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        [1, 2, None],
    ]

    for item in flat_generator(nested_list):
        print(item)
