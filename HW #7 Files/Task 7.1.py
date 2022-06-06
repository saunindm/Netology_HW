from pprint import pprint

with open('cook_book.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    while True:
        name = file.readline().rstrip()
        quantity = file.readline().rstrip()
        ingredients = []

        if not name or not quantity:
            break

        for item in range(int(quantity)):
            data = file.readline().strip()
            data = data.split('|')
            result = {'ingredient name': data[0], 'quantity': data[1], 'measure': data[2]}
            ingredients.append(result)
            cook_book[name] = ingredients
        file.readline()
    pprint(cook_book)

