import datetime
import json
import os

from node import *

date = datetime.date.today()
date_now = f'{date.day}.{date.month}.{date.year}'
zap1 = {'nodes': [{'title': 'Привет тест', 'body': 'Просто здороваюсь с тестом', 'date': date_now}]}
zap2 = {'id': 1, 'title': 'тест2222', 'body': 'Просто здороваюсь с тестом2222', 'date': '25.07.2023'}
zap3 = {'id': 1, 'title': 'Привет тест3333', 'body': 'Просто здороваюсь с тестом3333', 'date': date_now}
# print(zap1)
# with open("node.json", "w", encoding="utf-8") as f:
#     json.dump(zap1, f)
#     f.write('\n')

#
# with open('node.json', 'r', encoding='utf-8') as f:
#     text = json.load(f)
#     for i in range(0, len(text['nodes'])):
#         print(text['nodes'][i])


# --------------------------------------------------------------------------
# Дозапись в файл json
# with open('node.json', encoding='utf-8') as f:
#     text = json.load(f)
#     text['nodes'].append(zap3)
# with open('node.json', 'w', encoding='utf-8') as f1:
#     json.dump(text, f1, ensure_ascii=False, indent=2)

# -----------------------------------------------------------------------------

# --------------------------------------------------------------------------
# Удаление в файле json
# title1 = 'Привет тест'
# ind = 0
# with open('node.json', encoding='utf-8') as f:
#     text = json.load(f)
#     for i in text['nodes']:
#         if i['title'] == title1:
#             text['nodes'].remove(i)
#             print('удалил')
# with open('node.json', 'w', encoding='utf-8') as f1:
#     json.dump(text, f1, ensure_ascii=False, indent=2)

# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Сортировка по дате

# tmp = 1
# with open('node.json', encoding='utf-8') as f:
#     text = json.load(f)
#     while tmp != 0:
#         tmp = 0
#         for i in range(0, len(text['nodes']) - 1, 2):
#             tmp1 = datetime.datetime.strptime(text['nodes'][i]['date'], '%d.%m.%Y')
#             tmp2 = datetime.datetime.strptime(text['nodes'][i + 1]['date'], '%d.%m.%Y')
#             if tmp1 < tmp2:
#                 text['nodes'][i], text['nodes'][i + 1] = text['nodes'][i + 1], text['nodes'][i]
#                 tmp += 1
#     print(text)

# ------------------------------------------------------------------------------

node1 = Node()
# node1.creat('заметка 3', 'еще одна пробная заметка3')
#
# node1.remove(id_nod=1)
# node1.read_all()
# print('-' * 10)
# node1.sort_and_print_date()
# node1.chang_body(title='заметка 2', new_body='Измение заметки2')
# node1.chang_title(title='заметка 1', new_title='измененный загаловок1')
