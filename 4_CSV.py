import csv


answer = [{"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}]

with open('export.csv', 'w', encoding='utf-8') as f:
    fields = ['привет', 'как дела', 'пока']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for ans in answer:
        writer.writerow(ans)

# Вот эту штуку я доработаю еще=)
# new_dict = []
# with open('4937.txt', 'r', encoding='utf-8') as f:
#     fields = ['id', 'name', 'href']
#     reader = csv.DictReader(f, fields, delimiter='	')
#     for row in reader:
#         new_dict.append(row)
#     print(new_dict)