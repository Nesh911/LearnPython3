import csv


answer = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}

with open('export.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=':')
    for f in answer.items():
        writer.writerow(f)


# Вот эту штуку я доработаю еще=)
# new_dict = []
# with open('4937.txt', 'r', encoding='utf-8') as f:
#     fields = ['id', 'name', 'href']
#     reader = csv.DictReader(f, fields, delimiter='	')
#     for row in reader:
#         new_dict.append(row)
#     print(new_dict)