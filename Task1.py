from datetime import datetime


def make_log(old_function):
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)

        with open('log.txt', 'a') as logs_file:
            logs_file.write(f'Дата и время вызова функции: {datetime.today()}, имя функции: {old_function.__name__}, '
                            f'аргументы: {args} {kwargs}, возвращаемое значение: {result}\n')

        return result
    return new_function


@make_log
def summator(a, b, c):
    return a * b + c


if __name__ == '__main__':
    summator(10, 5, c=5)
