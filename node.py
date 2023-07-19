import datetime
import json


class Node:
    date = datetime.date.today()
    date_now = f'{date.day}.{date.month}.{date.year}'

    def creat(self, title, body):
        res = {'title': title, 'body': body, 'date': self.date_now}
        flag = 0
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
        with open('node.json', 'r', encoding='utf-8') as f:
            text = json.load(f)
            for i in text['nodes']:
                print('     ' + i['title'])
                print(i['body'])
                print(i['date'])

    def remove(self, title):
        flag = 0
        with open('node.json', encoding='utf-8') as f:
            text = json.load(f)
            for i in text['nodes']:
                if i['title'] == title:
                    text['nodes'].remove(i)
                    print('удалил')
                    flag += 1
        if flag != 0:
            with open('node.json', 'w', encoding='utf-8') as f1:
                json.dump(text, f1, ensure_ascii=False, indent=2)
        else:
            print('Совпадений не найдено!')

    def sort_date(self):
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
            print('     ' + i['title'])
            print(i['body'])
            print(i['date'])