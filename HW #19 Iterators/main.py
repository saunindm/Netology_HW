nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

nested_list1 = [
    [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        [
            ['g', 'h', 'i'],
            ['j', 'k', 'l'],
            ['m', 'n', 'o']
        ]
    ]
]


# 1. Итератор, который принимает список списков, и возвращает их плоское представление, т.е последовательность состоящую из вложенных элементов
class FlatIterator:
    def __init__(self, list):
        self.list = list

    def __iter__(self):
        self.i = -1
        self.flat_list = iter([])
        return self

    def __next__(self):
        try:
            item = next(self.flat_list)
        except StopIteration:
            self.i += 1
            if self.i == len(self.list):
                raise StopIteration
            self.flat_list = iter(self.list[self.i])
            item = next(self.flat_list)
        return item


# 2. Генератор, который принимает список списков, и возвращает их плоское представление
def flat_generator(nested_list):
    i = 0
    while i != len(nested_list):
        flat_list = nested_list[i]
        for item in flat_list:
            yield item
        i += 1


# 3.* Итератор аналогичный итератору из задания 1, но обрабатывающий списки с любым уровнем вложенности
class FlatIterator1:
    def __init__(self, nested_list):
        self.nested_list = nested_list

    def __iter__(self):
        self.i = -1
        self.cursor = iter([])
        return self

    def __next__(self):
        try:
            item = next(self.cursor)
        except StopIteration:
            self.i += 1
            if self.i == len(self.nested_list):
                raise StopIteration
            if isinstance(self.nested_list[self.i], list):
                nested = True
                while nested:
                    flat_list = []
                    nested = False
                    for item in self.nested_list[self.i]:
                        if isinstance(item, list):
                            flat_list.extend(item)
                            nested = True
                        else:
                            flat_list.append(item)
                    self.nested_list[self.i] = flat_list
                    self.cursor = iter(self.nested_list[self.i])
                item = next(self.cursor)
        return item


# 4.* Генератор аналогичный генератору из задания 2, но обрабатывающий списки с любым уровнем вложенности
def flat_generator1(nested_list):
    nested = True
    while nested:
        flat_list = []
        nested = False
        for i in nested_list:
            if isinstance(i, list):
                flat_list.extend(i)
                nested = True
            else:
                flat_list.append(i)
        nested_list = flat_list
    return flat_list


if __name__ == '__main__':
    # 1.
    for item in FlatIterator(nested_list):
        print(item)
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

    # 2.
    for item in flat_generator(nested_list):
        print(item)

    # 3.
    for item in FlatIterator1(nested_list1):
        print(item)
    flat_list = [item for item in FlatIterator1(nested_list1)]
    print(flat_list)

    # 4.
    for item in flat_generator1(nested_list1):
        print(item)
