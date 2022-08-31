from datetime import datetime


def cashe(file):
    def make_log(old_function, ):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)

            with open(file, 'a', encoding="utf-8") as logs_file:
                logs_file.write(f'Дата и время вызова функции: {datetime.today()}, имя функции: {old_function.__name__}, '
                                f'аргументы: {args} {kwargs}, возвращаемое значение: {result}\n')

            return result
        return new_function
    return make_log


@cashe(file='log2.txt')
def summator(a, b, c):
    return a * b + c


if __name__ == '__main__':
    summator(66, 3, c=15)
