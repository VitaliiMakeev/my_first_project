from node import Node


class View():
    node_pad = Node()

    def __init__(self):
        self.node_pad = Node()

    def menu(self):
        strlist = ['Выберите действие: ', '1. Создать заметку.', '2. Посмотреть все заметки.',
                   '3. Редактировать заметку.', '4. Удалить заметку.', '5. Сортировать по дате', '0. Выход.']
        for i in strlist:
            print(i)

    def dop_menu_edit(self):
        flag = 1
        while flag != 0:
            print('Как будем искать заметку?')
            print('1. По id заметки.')
            print('2. По названию заметки.')
            print('0. Выход.')
            try:
                n = int(input('Введите число: '))
                if 0 <= n <= 2:
                    return n
                else:
                    print('Необходимо ввести одну из цифр!(0-2)' + '\n' + 'Попробуйте еще раз.')
            except (Exception):
                print('Необходимо ввести одну из цифр!(0-2)' + '\n' + 'Попробуйте еще раз.')

    def input_id(self):
        flag = 1
        while flag != 0:
            try:
                n = int(input('Введите id: '))
                if n > 0:
                    return n
            except (Exception):
                print('Необходимо ввести целое число!(> 0)' + '\n' + 'Попробуйте еще раз.')

    def menu_edition_node(self):
        flag = 1
        while flag != 0:
            print('Что будем редактировать?')
            print('1. Название заметки.')
            print('2. Текст заметки.')
            print('0. Выход.')
            try:
                n = int(input('Введите число: '))
                if 0 <= n <= 2:
                    match n:
                        case 0:
                            flag = 0
                        case 1:
                            search = self.dop_menu_edit()
                            if search == 1:
                                id_nod1 = self.input_id()
                                text_title = input('Введите новое название заметки: ')
                                self.node_pad.chang_title(new_title=text_title, id_nod=id_nod1)
                            elif search == 2:
                                titl_text = input('Введите название искомой заметки: ')
                                new_text_titl = input('Введите новое название заметки: ')
                                self.node_pad.chang_title(new_title=new_text_titl, title=titl_text)
                        case 2:
                            search = self.dop_menu_edit()
                            if search == 1:
                                id_nod1 = self.input_id()
                                text_body = input('Введите новый текст заметки: ')
                                self.node_pad.chang_body(new_body=text_body, id_nod=id_nod1)
                            elif search == 2:
                                titl1 = input('Введите название искомой заметки: ')
                                new_text_body = input('Введите новое название заметки: ')
                                self.node_pad.chang_body(new_body=new_text_body, title=titl1)

                else:
                    print('Необходимо ввести одну из цифр!(0-2)' + '\n' + 'Попробуйте еще раз.')
            except (Exception):
                print('Необходимо ввести одну из цифр!(0-2)' + '\n' + 'Попробуйте еще раз.')

    def menu_creat_node(self):
        flag = 1
        flag1 = 1
        result = []
        while flag != 0:
            title_start = input('Введите название заметки: ')
            if len(title_start) <= 1:
                print('Слишком короткое название заметки!' + '\n' + 'Попробуйте еще раз.')
            else:
                result.append(title_start)
                flag = 0
        while flag1 != 0:
            body_start = input('Введите текст заметки: ')
            if len(body_start) <= 1:
                print('Слишком короткое сообщение!' + '\n' + 'Попробуйте еще раз.')
            else:
                result.append(body_start)
                flag1 = 0
        return result

    def menu_remove(self):
        search = self.dop_menu_edit()
        if search == 1:
            id_nod2 = self.input_id()
            self.node_pad.remove(id_nod=id_nod2)
        elif search == 2:
            title_name = input('Введите заголовок заметки: ')
            self.node_pad.remove(title=title_name)

    def start(self):
        print('Добро пожаловать!' + '\n' + 'Я запомню все что вы мне укажите!')
        flag = 1
        while flag != 0:
            self.menu()
            try:
                n = int(input())
                if 0 <= n <= 5:
                    match n:
                        case 0:
                            flag = 0
                        case 1:
                            res = self.menu_creat_node()
                            self.node_pad.creat(res[0], res[1])
                        case 2:
                            self.node_pad.read_all()
                        case 3:
                            self.menu_edition_node()
                        case 4:
                            self.menu_remove()
                        case 5:
                            self.node_pad.sort_and_print_date()
                else:
                    print('Необходимо ввести одну из цифр(0-5)!')
            except (Exception):
                print('Необходимо ввести одну из цифр(0-5)!')
