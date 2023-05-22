import os
import sys
from os import path
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem
import datetime
from ui.menu import Ui_MainWindowMenu
from ui.error import Ui_MainWindowError
from ui.fondir import Ui_MainWindowFonDir
from ui.dun import Ui_MainWindowDun
from ui.add import Ui_MainWindowAdd
from ui.red import Ui_MainWindowRed
from ui.export import Ui_MainWindowExp
from ui.imports import Ui_MainWindowImp


class StartMenu(QtWidgets.QMainWindow):
    def __init__(self):
        super(StartMenu, self).__init__()
        self.ui = Ui_MainWindowMenu()
        self.ui.setupUi(self)


class Error(QtWidgets.QMainWindow):
    def __init__(self):
        super(Error, self).__init__()
        self.ui = Ui_MainWindowError()
        self.ui.setupUi(self)


class Dun(QtWidgets.QMainWindow):
    def __init__(self):
        super(Dun, self).__init__()
        self.ui = Ui_MainWindowDun()
        self.ui.setupUi(self)


class Add(QtWidgets.QMainWindow):
    def __init__(self):
        super(Add, self).__init__()
        self.ui = Ui_MainWindowAdd()
        self.ui.setupUi(self)


class Red(QtWidgets.QMainWindow):
    def __init__(self):
        super(Red, self).__init__()
        self.ui = Ui_MainWindowRed()
        self.ui.setupUi(self)


class Exp(QtWidgets.QMainWindow):
    def __init__(self):
        super(Exp, self).__init__()
        self.ui = Ui_MainWindowExp()
        self.ui.setupUi(self)


class Imp(QtWidgets.QMainWindow):
    def __init__(self):
        super(Imp, self).__init__()
        self.ui = Ui_MainWindowImp()
        self.ui.setupUi(self)


class FoneDir(QtWidgets.QMainWindow):
    def __init__(self):
        super(FoneDir, self).__init__()
        self.ui = Ui_MainWindowFonDir()
        self.ui.setupUi(self)

        self.ui.tableWidget.setHorizontalHeaderLabels(('ID', 'ФИО', 'номер\nтелефона'))
        self.ui.tableWidget.setColumnWidth(1, 250)
        self.ui.tableWidget.setColumnWidth(2, 150)


all_data = []
last_id = 0
file_base = 'base.txt'
list_znak = ['.', ',', '-', ':', ';', '_', '+', '=', '!', '"',
            '&', '?', '<', '>', '@', '#', '$', '%', '^', '*', '(', ')', '/', '|', '{', '}', '[', ']', '№']


def restart_tabl(flag: True, array=None):
    if flag:
        row = 1
        row_t = 0
        colum_t = 0
        fone_dir.ui.tableWidget.setRowCount(0)
        fone_dir.ui.tableWidget.setColumnCount(0)
        fone_dir.ui.tableWidget.setColumnCount(3)
        fone_dir.ui.tableWidget.setHorizontalHeaderLabels(('ID', 'ФИО', 'номер\nтелефона'))
        fone_dir.ui.tableWidget.setColumnWidth(1, 250)
        fone_dir.ui.tableWidget.setColumnWidth(2, 150)
        for i in array:
            tmp = i.split(',')
            fone_dir.ui.tableWidget.setRowCount(row)
            fone_dir.ui.tableWidget.setItem(row_t, colum_t, QTableWidgetItem(tmp[0].strip()))
            colum_t += 1
            fone_dir.ui.tableWidget.setItem(row_t, colum_t, QTableWidgetItem(tmp[1].strip()))
            colum_t += 1
            fone_dir.ui.tableWidget.setItem(row_t, colum_t, QTableWidgetItem(tmp[2].strip()))
            row += 1
            row_t += 1
            colum_t = 0
    else:
        fone_dir.ui.tableWidget.setRowCount(0)
        fone_dir.ui.tableWidget.setColumnCount(0)
        fone_dir.ui.tableWidget.setColumnCount(3)
        fone_dir.ui.tableWidget.setHorizontalHeaderLabels(('ID', 'ФИО', 'номер\nтелефона'))
        fone_dir.ui.tableWidget.setColumnWidth(1, 250)
        fone_dir.ui.tableWidget.setColumnWidth(2, 150)


def read_records():
    global all_data, last_id

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split(',')[0])
            return all_data
        return []


def on_activ_name():
    row_t = fone_dir.ui.tableWidget.currentRow()    # корректная строка
    colum_t = fone_dir.ui.tableWidget.currentColumn()   #корректный столбик
    try:
        item_name = fone_dir.ui.tableWidget.item(row_t, colum_t).text()

        if ' ' in item_name and len(item_name) > 5:
            return item_name
        else:
            return False
    except:
        return False


def on_click_error_ok():
    error.hide()


def on_click_dun():
    dun.hide()


def on_click_start_fondir():
    fone_dir.ui.lineEdit.clear()
    global file_base
    if path.exists(file_base):
        read_records()
        if all_data:
            restart_tabl(True, array=all_data)
        else:
            restart_tabl(False)
    else:
        with open(f'{file_base}', 'w', encoding='utf-8') as _:
            pass
    start.hide()
    fone_dir.show()


def on_click_fondir_back():
    fone_dir.hide()
    start.show()


def on_click_fondir_add():
    add.ui.lineEdit.clear()
    add.ui.lineEdit_2.clear()
    fone_dir.hide()
    add.show()


def on_click_add_back():
    add.hide()
    fone_dir.show()


def on_click_add_add():
    global last_id
    name = add.ui.lineEdit.text()
    fone_number = add.ui.lineEdit_2.text()
    k = 0
    if len(name) > 5:
        for i in list_znak:
            if i in name:
                k += 1
                error.ui.label.setText('В ФИО есть недопустимые символы!')
                error.show()
        for j in range(10):
            if str(j) in name:
                k += 1
                error.ui.label.setText('Нельзя цифры в ФИО!')
                error.show()
    else:
        k += 1
        error.ui.label.setText('Слишком короткое ФИО!')
        error.show()
    if len(fone_number) == 11:
        try:
            int(fone_number)
        except:
            k += 1
            error.ui.label.setText('В номере недопустимые символы!')
            error.show()
    else:
        k += 1
        error.ui.label.setText('Слишком короткий номер!')
        error.show()
    if k == 0:
        s = 0
        for n in all_data:
            if fone_number in n:
                s += 1
                error.ui.label.setText('Этот номер уже занят!')
                error.show()
        if s == 0:
            last_id += 1
            res = f'{last_id}, {name}, {fone_number}\n'
            with open(f'{file_base}', 'a', encoding='utf-8') as f:
                f.write(res)
            read_records()
            restart_tabl(True, array=all_data)
            add.ui.lineEdit.clear()
            add.ui.lineEdit_2.clear()
            dun.show()


def on_click_fondir_sourch():
    text = fone_dir.ui.lineEdit.text()
    tmp_list = []
    for i in all_data:
        if text in i:
            tmp_list.append(i)
    if tmp_list:
        restart_tabl(True, array=tmp_list)
    else:
        error.ui.label.setText('Совпадений не найдено!')
        error.show()


def on_click_fondir_clear():
    fone_dir.ui.lineEdit.clear()
    restart_tabl(True, array=all_data)


def on_click_fondir_del():
    name = on_activ_name()
    if name:
        tmp_list = []
        for i in all_data:
            if name not in i:
                tmp_list.append(i)
        with open(f'{file_base}', 'w', encoding='utf-8') as f:
            for j in tmp_list:
                f.write(f'{j}\n')
        read_records()
        restart_tabl(True, array=all_data)
        dun.show()
    else:
        error.ui.label.setText('Нажмите на ФИО того, кого удалить!')
        error.show()


tmp_data = []


def on_click_fondir_red():
    global tmp_data
    name = on_activ_name()
    if name:
        for i in all_data:
            if name in i:
                tmp_data = i.strip().split(",")
                res = f'{tmp_data[1]}, {tmp_data[2]}'
                red.ui.label_3.setText(res)
        fone_dir.hide()
        red.show()
    else:
        error.ui.label.setText('Выберите ФИО!')
        error.show()


def on_click_red_back():
    red.hide()
    fone_dir.show()


def on_click_red_save():
    global last_id, tmp_data
    old_name = tmp_data[1].strip()
    old_number = tmp_data[2].strip()
    enter_name = red.ui.lineEdit.text()
    enter_fone_number = red.ui.lineEdit_2.text()
    k = 0
    if len(enter_name) > 5:
        for i in list_znak:
            if i in enter_name:
                k += 1
                error.ui.label.setText('В ФИО есть недопустимые символы!')
                error.show()
        for j in range(10):
            if str(j) in enter_name:
                k += 1
                error.ui.label.setText('Нельзя цифры в ФИО!')
                error.show()
    else:
        k += 1
        error.ui.label.setText('Слишком короткое ФИО!')
        error.show()
    if len(enter_fone_number) == 11:
        try:
            int(enter_fone_number)
        except:
            k += 1
            error.ui.label.setText('В номере недопустимые символы!')
            error.show()
    else:
        k += 1
        error.ui.label.setText('Слишком короткий номер!')
        error.show()
    if k == 0:
        s = 0
        new_data = []
        if old_name == enter_name and old_number == enter_fone_number:
            error.ui.label.setText('Ничего не изменили!')
            error.show()
        else:
            for n in all_data:
                if old_name not in n:
                    new_data.append(n)
            for g in new_data:
                if enter_fone_number in g:
                    s += 1
                    error.ui.label.setText('Этот номер уже занят!')
                    error.show()
                    break
        if s == 0:
            last_id += 1
            res = f'{last_id}, {enter_name}, {enter_fone_number}'
            new_data.append(res)
            with open(f'{file_base}', 'w', encoding='utf-8') as f:
                for u in new_data:
                    f.write(f'{u}\n')
            read_records()
            restart_tabl(True, array=all_data)
            red.ui.lineEdit.clear()
            red.ui.lineEdit_2.clear()
            dun.show()


def on_click_start_export():
    read_records()
    start.hide()
    export.show()


def on_click_exp_back():
    export.ui.label_2.setText(f'Имя файла:')
    export.ui.label_3.setText(f'Путь до нового фала:')
    export.hide()
    start.show()


file_base_new = ''
directory = ''


def on_click_exp_tac_dir():
    global file_base_new, directory
    directory = QtWidgets.QFileDialog.getExistingDirectory(export, "Выберите папку")
    date_now_1 = str(date_now).replace('-', '')
    file_base_new = f'{date_now_1}{file_base}'
    export.ui.label_2.setText(f'Имя файла: {file_base_new}')
    export.ui.label_3.setText(f'Путь до нового фала: {directory}')


def on_click_exp_exp():
    global file_base_new, directory
    if all_data:
        if directory:
            if os.path.isfile(f'{directory}/{file_base_new}'):
                os.remove(f'{directory}/{file_base_new}')
            with open(f'{directory}/{file_base_new}', 'w', encoding='utf-8') as f:
                for i in all_data:
                    tmp_list = i.split(',')
                    f.write(f'{tmp_list[1].strip()}, {tmp_list[2].strip()}\n')
            dun.show()
        else:
            error.ui.label.setText('Выберите путь сохранения!!')
            error.show()
    else:
        error.ui.label.setText('База пока пустая!')
        error.show()


def on_click_imp_back():
    imports.ui.label_2.setText(f'Имя файла:')
    imports.ui.label_3.setText(f'Путь до нового фала:')
    imports.hide()
    start.show()


def on_click_start_import():
    read_records()
    start.hide()
    imports.show()


tmp_list = []


def on_click_imp_tac_file():
    global tmp_list
    filename, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Open File", ".", "Text Files (*.txt);;All Files (*)")
    filename_fin = filename.split('/')[-1]
    if filename:
        with open(f'{filename}', 'r', encoding='utf-8') as f:
            tmp_list = [i.strip() for i in f]
    imports.ui.label_2.setText(f'Имя файла: {filename_fin}')
    imports.ui.label_3.setText(f'Путь до нового фала: {filename}')


def on_click_imp_imp():
    global last_id
    result_list = []
    count = 0
    if tmp_list:
        for i in tmp_list:
            tmp_1 = i.split(',')
            tmp_count = 0
            for l in all_data:
                if tmp_1[1].strip() in l:           #проверяю только уникальность номера
                    tmp_count += 1                  # т.к. у одного человека может быть несколько номеров
                    count += 1
            if tmp_count == 0:
                last_id += 1
                result_list.append(f'{last_id}, {tmp_1[0].strip()}, {tmp_1[1].strip()}')
        if result_list:
            with open(f'{file_base}', 'a', encoding='utf-8') as f:
                for j in result_list:
                    f.write(f'{j}\n')

            read_records()
            dun.show()
        else:
            error.ui.label.setText('Не добавленно ни одной записи!')
            error.show()
        if count != 0:
            error.ui.label.setText(f'{count} записей имют такие же ФИО или номер!')
            error.show()


app = QtWidgets.QApplication([])
start = StartMenu()
error = Error()
fone_dir = FoneDir()
dun = Dun()
add = Add()
red = Red()
export = Exp()
imports = Imp()

date_now = datetime.date.today()
start_labl = f'Добро пожаловать!\nСегодня: {date_now.day}.{date_now.month}.{date_now.year}'
start.ui.label.setText(start_labl)
start.show()

start.ui.pushButton_8.clicked.connect(app.quit)
start.ui.pushButton.clicked.connect(on_click_start_fondir)
start.ui.pushButton_6.clicked.connect(on_click_start_export)
start.ui.pushButton_7.clicked.connect(on_click_start_import)

dun.ui.pushButton.clicked.connect(on_click_dun)
error.ui.pushButton.clicked.connect(on_click_error_ok)

fone_dir.ui.pushButton_2.clicked.connect(on_click_fondir_back)
fone_dir.ui.pushButton_5.clicked.connect(on_click_fondir_add)
fone_dir.ui.pushButton.clicked.connect(on_click_fondir_sourch)
fone_dir.ui.pushButton_6.clicked.connect(on_click_fondir_clear)
fone_dir.ui.pushButton_4.clicked.connect(on_click_fondir_del)
fone_dir.ui.pushButton_3.clicked.connect(on_click_fondir_red)

add.ui.pushButton.clicked.connect(on_click_add_back)
add.ui.pushButton_2.clicked.connect(on_click_add_add)

red.ui.pushButton_2.clicked.connect(on_click_red_back)
red.ui.pushButton.clicked.connect(on_click_red_save)

export.ui.pushButton_3.clicked.connect(on_click_exp_back)
export.ui.pushButton.clicked.connect(on_click_exp_tac_dir)
export.ui.pushButton_2.clicked.connect(on_click_exp_exp)

imports.ui.pushButton_3.clicked.connect(on_click_imp_back)
imports.ui.pushButton.clicked.connect(on_click_imp_tac_file)
imports.ui.pushButton_2.clicked.connect(on_click_imp_imp)

sys.exit(app.exec())