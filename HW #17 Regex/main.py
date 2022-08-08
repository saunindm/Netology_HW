import csv
import re

with open("phonebook_raw.csv", "r", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts = list(rows)

# We can make this file beautiful and searchable if this error is corrected: It looks like row 5 should actually have 7
# columns, instead of 8. in line 4.
contacts[4].pop(7)

# 1. Поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно. В записной книжке
# изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О;
pattern1 = r"^(\w*)[,\s](\w*)[,\s]?(\w*)?"
for contact in contacts[1:]:
    temp_str = ','.join(contact[0:3])
    temp_list = re.sub(pattern1, "\\1,\\2,\\3", temp_str).split(',')
    contact[0] = temp_list[0]
    contact[1] = temp_list[1]
    contact[2] = temp_list[2]

# 2. Привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999;
pattern2 = r"(\+7|8)\s*\(?(495)\)?[-\s]?(\d{3,3})[-\s]?(\d{2,2})[-\s]?(\d{2,2})(\s)?\(?(доб.)?\s?(\d{4,4})?\)?"
for contact in contacts:
    contact[5] = re.sub(pattern2, "+7(\\2)\\3-\\4-\\5\\6\\7\\8", contact[5])

# 3. Объединить все дублирующиеся записи о человеке в одну.
temp_list = []
for contact in contacts:
    if contact[0] in temp_list:
        i = temp_list.index(contact[0])
        for j, el in enumerate(contact):
            if el != '':
                contacts[i][j] = el
                contact[j] = ''
    temp_list.append(contact[0])
contacts = [contact for contact in contacts if contact[0] != '']  # удалить пустые записи

with open("phonebook.csv", "w", encoding='utf-8', newline="") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts)
