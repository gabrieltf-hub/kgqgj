from PyQt5.QtWidgets import QWidget, QFileDialog

import csv
import os

from ui.main_widget import Ui_MainWin


class MainWin_Ui(Ui_MainWin):
    def __init__(self, parent=None):
        self.w = QWidget(parent=parent)
        self.setupUi(self.w)
        # 信号槽与绑定
        self.searchFileButton.clicked.connect(self.select_file_msg)

        self.resetButton.clicked.connect(lambda _: self.searchFilelineEdit.setText(""))
        self.acceptButton.clicked.connect(self.accept_msg)

    def accept_msg(self):
        input_filename = self.searchFilelineEdit.text().strip()
        output_filename, _ = os.path.splitext(input_filename)
        output_filename += ".csv"

        f = open(input_filename, encoding="utf-8")
        data = f.readlines()
        f.close()
        data = [i.strip() for i in data if i.strip() != '']
        start_index = 0
        data_list = []
        while start_index < len(data):
            end_index = start_index + int(data[start_index + 1]) * 3 + 3
            data_list.append(data[start_index: end_index])
            start_index = end_index

        boss_names = set()
        for i in data_list:
            for j in range(len(i)):
                if i[j].isdigit():
                    i[j] = int(i[j])
            boss_names.add(i[4])
            try:
                boss_names.add(i[7])
            except IndexError:
                pass
            try:
                boss_names.add(i[10])
            except IndexError:
                pass
        boss_names = list(boss_names)

        d = dict()
        for i in data_list:
            name = i[0]
            if name not in d:
                d[name] = [0] * 10
            d[name][0] += i[1]
            d[name][1] += i[2]
            for num in range(int(i[1])):
                for j in range(len(boss_names)):
                    boss_name = boss_names[j]
                    if i[num * 3 + 4] == boss_name:
                        d[name][j * 2 + 2] += 1
                        d[name][j * 2 + 3] += i[num * 3 + 3]

        table_head = ["昵称", "总刀数", "总伤害数",
                      boss_names[0] + "刀数", boss_names[0] + "伤害数",
                      boss_names[1] + "刀数", boss_names[1] + "伤害数",
                      boss_names[2] + "刀数", boss_names[2] + "伤害数",
                      boss_names[3] + "刀数", boss_names[3] + "伤害数"]
        res = [table_head]
        res.extend([[k] + v for k, v in d.items()])

        with open(output_filename, 'w', newline="") as csvfile:
            w = csv.writer(csvfile)
            w.writerows(res)

    def select_file_msg(self):
        filename = QFileDialog.getOpenFileName(None, "请选择文件", "", "All Files (*);;Text Files (*.txt)")
        if filename:
            self.searchFilelineEdit.setText(filename[0])

    def show(self):
        self.w.show()
