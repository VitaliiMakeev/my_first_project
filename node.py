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
        else:
            with open('node.json', encoding='utf-8') as f1:
                text = json.load(f1)
                if len(text['nodes']) != 0:
                    self.id_node = text['nodes'][-1]['id']

    def creat(self, title, body):
        res = {'id': self.id_node + 1, 'title': title, 'body': body, 'date': self.date_now}
        flag = 0
        if self.id_node == 0:
            result = {'nodes': [res]}
            with open('node.json', 'w', encoding='utf-8') as f1:
                json.dump(result, f1, ensure_ascii=False, indent=2)
                self.id_node += 1
        else:
            with open('node.json', encoding='utf-8') as f:
                text = json.load(f)
                for i in text['nodes']:
                    if i['title'] == title:
                        print('Такой заголовок уже есть! придумайте другой.')
                        flag += 1
            if flag == 0:
                self.id_node += 1
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
                    print('№' + str(i['id']) + '     ' + i['title'])
                    print(i['body'])
                    print(i['date'])
                    print('-' * len(i['body']) + (10 * '-'))

    def remove(self, title=None, id_nod=None):
        flag = 0
        if self.id_node == 0:
            print('Список заметок пуст!')
        else:
            if title:
                with open('node.json', encoding='utf-8') as f:
                    text = json.load(f)
                    for i in text['nodes']:
                        if i['title'] == title:
                            text['nodes'].remove(i)
                            print('Удалил!')
                            flag += 1
                            break
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
                            break
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
                print('№' + str(i['id']) + '     ' + i['title'])
                print(i['body'])
                print(i['date'])

    def chang_body(self, new_body, id_nod=None, title=None):
        if self.id_node == 0:
            print('Список заметок пуст!')
        else:
            flag = 0
            if id_nod:
                with open('node.json', encoding='utf-8') as f:
                    text = json.load(f)
                    for i in range(0, len(text['nodes'])):
                        if text['nodes'][i]['id'] == id_nod:
                            text['nodes'][i]['body'] = new_body
                            text['nodes'][i]['date'] = self.date_now
                            print('Готово!')
                            flag += 1
                            break
                if flag != 0:
                    with open('node.json', 'w', encoding='utf-8') as f1:
                        json.dump(text, f1, ensure_ascii=False, indent=2)
                else:
                    print('Совпадений не найдено!')
            if title:
                with open('node.json', encoding='utf-8') as f:
                    text = json.load(f)
                    for i in range(0, len(text['nodes'])):
                        if text['nodes'][i]['title'] == title:
                            text['nodes'][i]['body'] = new_body
                            text['nodes'][i]['date'] = self.date_now
                            print('Готово!')
                            flag += 1
                            break
                if flag != 0:
                    with open('node.json', 'w', encoding='utf-8') as f1:
                        json.dump(text, f1, ensure_ascii=False, indent=2)
                else:
                    print('Совпадений не найдено!')

    def chang_title(self, new_title: str, id_nod=None, title=None):
        if self.id_node == 0:
            print('Список заметок пуст!')
        else:
            flag = 0
            if id_nod:
                with open('node.json', encoding='utf-8') as f:
                    text = json.load(f)
                    for i in range(0, len(text['nodes'])):
                        if text['nodes'][i]['id'] == id_nod:
                            text['nodes'][i]['title'] = new_title
                            text['nodes'][i]['date'] = self.date_now
                            print('Готово!')
                            flag += 1
                            break
                if flag != 0:
                    with open('node.json', 'w', encoding='utf-8') as f1:
                        json.dump(text, f1, ensure_ascii=False, indent=2)
                else:
                    print('Совпадений не найдено!')
            if title:
                with open('node.json', encoding='utf-8') as f:
                    text = json.load(f)
                    for i in range(0, len(text['nodes'])):
                        if text['nodes'][i]['title'] == title:
                            text['nodes'][i]['title'] = new_title
                            text['nodes'][i]['date'] = self.date_now
                            print('Готово!')
                            flag += 1
                            break
                if flag != 0:
                    with open('node.json', 'w', encoding='utf-8') as f1:
                        json.dump(text, f1, ensure_ascii=False, indent=2)
                else:
                    print('Совпадений не найдено!')

    def search_date(self, search_date):
        res = []
        if self.id_node == 0:
            print('Список заметок пуст!')
        else:
            with open('node.json', encoding='utf-8') as f:
                text = json.load(f)
                for i in text['nodes']:
                    if i['date'] == search_date:
                        res.append(i)
        return res

    def search_title(self, serch_title):
        res = []
        if self.id_node == 0:
            print('Список заметок пуст!')
        else:
            with open('node.json', encoding='utf-8') as f:
                text = json.load(f)
                for i in text['nodes']:
                    if i['title'] == serch_title:
                        res.append(i)
        return res

    def search_id(self, id_nod8):
        res = []
        if self.id_node == 0:
            print('Список заметок пуст!')
        else:
            with open('node.json', encoding='utf-8') as f:
                text = json.load(f)
                for i in text['nodes']:
                    if i['id'] == id_nod8:
                        res.append(i)
        return res