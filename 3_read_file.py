# # Задание - Прочитайте его и подсчитайте количество слов в тексте файла 'referat.txt'
#
# def read_file():
#     with open('referat.txt', 'r', encoding='utf-8') as f:
#         print(str(sum(1 for i in f)) + ' строк в файле, включая пустые')
#
#
# def read_file2():
#     final_list = []
#     with open('referat.txt', 'r', encoding='utf-8') as f:
#         for line in f:
#             if not line.isspace():
#                 word = line.split(' ')
#                 for i in word:
#                     final_list.append(i.strip())
#     print(str(len(final_list)) + ' слова в тексте')
#
# read_file()
# read_file2()
