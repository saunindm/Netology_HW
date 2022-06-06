from pprint import pprint


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        with open('cook_book.txt', 'r', encoding='utf-8') as file:
            for line in file:
                if dish in line:
                    quantity = file.readline().rstrip()
                    for item in range(int(quantity)):
                        data = file.readline().strip()
                        data = data.split('|')
                        if data[0] in shop_list.keys():
                            shop_list[data[0]]['quantity'] += int(data[1]) * person_count
                        else:
                            shop_list[data[0]] = {'measure': data[2], 'quantity': int(data[1]) * person_count}
                    file.readline()
    return shop_list


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
print()
pprint(get_shop_list_by_dishes(['Омлет'], 3))
print()
pprint(get_shop_list_by_dishes(['Омлет', 'Омлет', 'Омлет'], 1))
print()
pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))
