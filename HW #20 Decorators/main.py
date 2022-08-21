from habr_parser import habr_parser


# TODO: 1. Написать декоратор - логгер. Он записывает в файл дату и время вызова функции, имя функции, аргументы, с которыми вызвалась и возвращаемое значение.
#       2. Написать декоратор из п.1, но с параметром – путь к логам.
#       3. Применить написанный логгер к приложению из любого предыдущего д/з.


if __name__ == '__main__':
    print(habr_parser(keywords=['Python']))
    print(habr_parser(keywords=['Github']))
    print(habr_parser(keywords=['Django']))
