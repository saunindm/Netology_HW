class Stack:
    '''Стек - абстрактный тип данных, представляющий собой список элементов, организованных по принципу LIFO (англ. last in — first out, «последним пришёл — первым вышел»).
    Чаще всего принцип работы стека сравнивают со стопкой тарелок: чтобы взять вторую сверху, нужно снять верхнюю. Или с магазином в огнестрельном оружии (стрельба начнётся с
    патрона, заряженного последним).
    '''

    def __init__(self, stack):
        self.stack = stack

    def isEmpty(self):
        '''проверка стека на пустоту. Метод возвращает True или False.
        '''
        if not self.stack:
            return True
        return False

    def push(self, element):
        '''добавляет новый элемент на вершину стека. Метод ничего не возвращает.
        '''
        self.stack.append(element)

    def pop(self):
        '''удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
        '''
        self.stack.pop(-1)

    def peek(self):
        '''возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
        '''
        return self.stack[-1]

    def size(self):
        '''возвращает количество элементов в стеке.
        '''
        return len(self.stack)


if __name__ == '__main__':
    temp_list = []
    stack = Stack(temp_list)
    print(stack.isEmpty())
    stack.push('Hello')
    stack.push(24)
    print(temp_list)
    stack.pop()
    print(stack.peek())
    print(stack.size())
