from functools import wraps
from datetime import datetime


def logger(file_path):

    def _logger(old_function, ):

        @wraps(old_function)
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            with open(file_path, 'a', encoding='cp1251') as file:
                data = (
                    f"Время вызова функции: {datetime.now()}\n"
                    f"Вызвана функция {old_function.__name__} с аргументами {args} и {kwargs}\n"
                    f"Результат:\n{result}\n"
                )
                file.write(data)
            return data

        return new_function

    return _logger
