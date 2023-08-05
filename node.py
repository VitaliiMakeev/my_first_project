import datetime
import json
import os
from os import listdir
from os.path import isfile, join


class Node:
    date = datetime.date.today()
    date_now = f'{date.day}.{date.month}.{date.year}'
    id_node = 0

    def __init__(self):
        mypath = os.getcwd()
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        k = 0
        for j in onlyfiles:
            if j == 'node.json':
                k += 1
        if k == 0:
            data = {'nodes': []}
            with open('node.json', 'w', encoding='utf-8') as f:
                json.dump(data, f)
                # f.write('\n')
                print('Добро пожаловать!' + '\n' + 'Я запомню все, что вы мне дадите!')
        else:
            with open('node.json', encoding='utf-8') as f:
                text = json.load(f)
                for i in text['nodes']:
                    self.id_node = i['id']

    def creat(self, title, body):
        res = {'id': self.id_node + 1, 'title': title, 'body': body, 'date': self.date_now}
        flag = 0
        if self.id_node == 0:
            result = {'nodes': [res]}
            with open('node.json', 'w', encoding='utf-8') as f1:
                json.dump(result, f1, ensure_ascii=False, indent=2)
        else:
            with open('node.json', encoding='utf-8') as f:
                text = json.load(f)
                for i in text['nodes']:
                    if i['title'] == title:
                        print('Такой заголовок уже есть! придумайте другой.')
                        flag += 1
            if flag == 0:
                text['nodes'].append(res)
                with open('node.json', 'w', encoding='utf-8') as f1:
                    json.dump(text, f1, ensure_ascii=False, indent=2)

    def read_all(self):
        if self.id_node == 0:
            print('Список заметок пуст!')
        else:
            with open('node.json', 'r', encoding='utf-8') as f:
                text = json.load(f)
                for i in text['nodes']:
                    print(str(i['id']) + '     ' + i['title'])
                    print(i['body'])
                    print(i['date'])

    def remove(self, title=None, id_nod=None):
        flag = 0
        if self.id_node == 0:
            print('Список заметок пуст!')
        else:
            if title == None and id_nod == None:
                print('Необходнимо указать id заметки или загаловок!')
            elif title:
                with open('node.json', encoding='utf-8') as f:
                    text = json.load(f)
                    for i in text['nodes']:
                        if i['title'] == title:
                            text['nodes'].remove(i)
                            print('Удалил!')
                            flag += 1
                if flag != 0:
                    with open('node.json', 'w', encoding='utf-8') as f1:
                        json.dump(text, f1, ensure_ascii=False, indent=2)
                else:
                    print('Совпадений не найдено!')
            elif id_nod:
                with open('node.json', encoding='utf-8') as f:
                    text = json.load(f)
                    for i in text['nodes']:
                        if i['id'] == id_nod:
                            text['nodes'].remove(i)
                            print('Удалил!')
                            flag += 1
                if flag != 0:
                    with open('node.json', 'w', encoding='utf-8') as f1:
                        json.dump(text, f1, ensure_ascii=False, indent=2)
                else:
                    print('Совпадений не найдено!')

    def sort_and_print_date(self):
        if self.id_node == 0:
            print('Список заметок пуст!')
        else:
            tmp = 1
            with open('node.json', encoding='utf-8') as f:
                text = json.load(f)
                while tmp != 0:
                    tmp = 0
                    for i in range(0, len(text['nodes']) - 1, 2):
                        tmp1 = datetime.datetime.strptime(text['nodes'][i]['date'], '%d.%m.%Y')
                        tmp2 = datetime.datetime.strptime(text['nodes'][i + 1]['date'], '%d.%m.%Y')
                        if tmp1 < tmp2:
                            text['nodes'][i], text['nodes'][i + 1] = text['nodes'][i + 1], text['nodes'][i]
                            tmp += 1
            for i in text['nodes']:
                print(str(i['id']) + '     ' + i['title'])
                print(i['body'])
                print(i['date'])
