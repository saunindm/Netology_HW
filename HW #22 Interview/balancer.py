from stack import Stack


brackets_dict = {'{': '}', '[': ']', '(': ')'}
op_br = '[{('
cl_br = '}])'
temp_list = []


class Balancer(Stack):

    def isBalanced(self, sequence):
        self.stack = Stack(temp_list)
        for el in sequence:
            if el in op_br:
                self.stack.push(el)
            elif el in cl_br:
                if self.stack.isEmpty():
                    return 'Несбалансированно: нет парной открывающей'
                else:
                    if brackets_dict[self.stack.peek()] == el:
                        self.stack.pop()
                    else:
                        return 'Несбалансированно: скобка открылась и не закрылась'
        if self.stack.isEmpty():
            return 'Сбалансированно: последовательность скобок корректная.'
        return 'Несбалансированно: скобка открылась и не закрылась.'


if __name__ == '__main__':
    sequence = Balancer([])
    seq_list = [
        '(((([{}]))))',
        '[([])((([[[]]])))]{()}',
        '{{[()]}}',
        '}{}',
        '{{[(])]}}',
        '[[{())}]'
    ]
    for seq in seq_list:
        print(f"{seq} --- {sequence.isBalanced(seq)}")
