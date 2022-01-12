# import schedule
# import time
from db_ops import *

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import sys

from win32api import GetSystemMetrics


class Task:
    def __init__(self, time, task_text):
        self.task: str = " - ".join([time, task_text])

    def __str__(self):
        return self.task


class Day:
    tasks = []

    def __init__(self, day_name):
        self.day_name = day_name
        self.day_obj: object
        self.set_day_obj()
        self.tasks: list = []
        self.day_tasks: dict = {self.day_name: self.tasks}
        self.fill_tasks()

    def set_day_obj(self):
        if self.day_name == "MONDAY":
            self.day_obj = Monday
        elif self.day_name == "TUESDAY":
            self.day_obj = Tuesday
        elif self.day_name == "WEDNESDAY":
            self.day_obj = Wednesday
        elif self.day_name == "THURSDAY":
            self.day_obj = Thursday
        elif self.day_name == "FRIDAY":
            self.day_obj = Friday
        elif self.day_name == "SATURDAY":
            self.day_obj = Saturday
        elif self.day_name == "SUNDAY":
            self.day_obj = Sunday

    def fill_tasks(self):
        with db:
            for k in self.day_obj.select(self.day_obj.task):
                self.tasks.append(k.task)

    def add_task(self, time, task_text):
        with db:
            local_task = Task(time, task_text)
            self.day_obj.insert(task=local_task).execute()

    def remove_task(self, full_task_text):
        with db:
            self.day_obj.delete().where(task=full_task_text).execute()


class Week:
    days_list: list[Day]

    def __init__(self):
        self.monday = Day("MONDAY")
        self.tuesday = Day("TUESDAY")
        self.wednesday = Day("WEDNESDAY")
        self.thursday = Day("THURSDAY")
        self.friday = Day("FRIDAY")
        self.saturday = Day("SATURDAY")
        self.sunday = Day("SUNDAY")
        self.days_list = [
            self.monday, self.tuesday, self.wednesday,
            self.thursday, self.friday, self.saturday, self.sunday
        ]


class Assembly(QWidget):
    SCREEN_W = GetSystemMetrics(0) // 1.2
    SCREEN_H = GetSystemMetrics(1) // 1.8

    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #293133")
        self.setGeometry(300, 300, self.SCREEN_W, self.SCREEN_H)

        self.set_default_size_button = QPushButton(self)
        self.set_default_size_button.clicked.connect(self.set_default_size)
        self.set_default_size_button.setText("Set Default Size")
        self.set_default_size_button.setGeometry(self.SCREEN_W * 0.865, 7, self.SCREEN_W // 9, self.SCREEN_H // 20)
        self.set_default_size_button.setStyleSheet("QPushButton\
                         {background-color: #8b00ff; border-radius: 10px; font: bold 14px;min-width: 3em; padding: 1px;\
                          color: white;}"
                                                   "QPushButton:pressed { background-color: #990000; border-radius: "
                                                   "10px;\
                                            font: bold 14px;min-width: 3em; padding: 1px; color: white;}"
                                                   "QPushButton:pressed { background-color: #6600ff; border-radius: "
                                                   "10px;\
                                                    font: bold 14px;min-width: 3em; padding: 1px; color: white;}")
        self.set_default_size_button.show()

        self.show()
        self.widget: object
        self.day_column: object
        self.task_column: object
        self.complete_button: object
        self.cancel_button: object
        self.draw_columns()
        self.draw_day_names()
        self.draw_add_tasks_buttons()
        self.draw_tasks()

    def set_default_size(self):
        self.resize(self.SCREEN_W, self.SCREEN_H)

    def draw_columns(self):
        column_list = Week()
        __x = self.SCREEN_W // 160
        __y = self.SCREEN_H // 15
        __w = self.SCREEN_W // 7.8
        __h = self.SCREEN_H * 4
        __column_space = self.SCREEN_W // 70
        __day_count = 1
        for _ in column_list.days_list:
            self.column_label = QLabel(self)
            self.column_label.setGeometry(__x, __y, __w, __h)

            if __day_count > 5:
                self.column_label.setStyleSheet("background-color: pink; border-radius: 10px; font: bold 14px;")
            else:
                self.column_label.setStyleSheet("background-color: lightgreen; border-radius: 10px; font: bold 14px;")

            self.column_label.show()

            __x = __x + __w + __column_space
            __day_count += 1

    def draw_day_names(self):
        column_list = Week()
        __x = self.SCREEN_W // 85
        __y = self.SCREEN_H // 13
        __w = self.SCREEN_W // 8.5
        __h = self.SCREEN_H // 28
        __column_space = self.SCREEN_W // 41
        __day_count = 1
        for i in column_list.days_list:
            self.day_name_label = QLabel(self)
            self.day_name_label.setGeometry(__x, __y, __w, __h)
            self.day_name_label.setAlignment(Qt.AlignHCenter)
            if __day_count > 5:
                self.day_name_label.setStyleSheet("background-color: #ff0000; border-radius: 10px; font: bold 14px;\
                min-width: 3em; padding: 1px; color: white")
            else:
                self.day_name_label.setStyleSheet("background-color: green; border-radius: 10px; font: bold 14px;\
                                        min-width: 3em; padding: 1px; color: white;")

            self.day_name_label.setText(i.day_name)
            self.day_name_label.show()
            __x = __x + __w + __column_space
            __day_count += 1

    def draw_add_tasks_buttons(self):
        __x = self.SCREEN_W // 85
        __y = self.SCREEN_H // 8
        __w = self.SCREEN_W // 8.5
        __h = self.SCREEN_H // 28
        __column_space = self.SCREEN_W // 41
        __day_count = 1
        for i, k in enumerate(Week().days_list):
            self.add_task_button = QPushButton(self)
            self.add_task_button.setGeometry(__x + __w // 9, __y, __w * 0.8, __h)
            self.add_task_button.setText("Add new task")
            if __day_count > 5:
                self.add_task_button.setStyleSheet("QPushButton\
                 {background-color: #ff0000; border-radius: 10px; font: bold 14px;min-width: 3em; padding: 1px;\
                  color: white;}"
                                                   "QPushButton:pressed { background-color: #990000; border-radius: "
                                                   "10px;\
                                                    font: bold 14px;min-width: 3em; padding: 1px; color: white;}")
            else:
                self.add_task_button.setStyleSheet("QPushButton\
                 {background-color: green; border-radius: 10px; font: bold 14px;min-width: 3em; padding: 1px;\
                  color: white;}"
                                                   "QPushButton:pressed { background-color: #004d00;"
                                                   "border-radius: 10px;font: bold 14px;min-width: 3em;\
                                                 padding: 1px; color: white;}")

            self.add_task_button.clicked.connect(Week().days_list[i].add_task("19:20", "hello worыld"))
            self.add_task_button.clicked.connect(self.draw_tasks)
            self.add_task_button.clicked.connect(self.draw_add_tasks_buttons)
            self.add_task_button.show()
            __x = __x + __w + __column_space
            __day_count += 1

    def draw_tasks(self):
        Week()
        __x = self.SCREEN_W // 85
        __y = self.SCREEN_H // 5
        __w = self.SCREEN_W // 8.5
        __h = self.SCREEN_H // 14
        __column_space = self.SCREEN_W // 41
        __day_count = 1
        for i in Week().days_list:
            for k in i.tasks:
                self.task_complete_button = QPushButton(self)
                self.task_complete_button.setGeometry(__x, __y, __w, __h)
                self.task_complete_button.setText(str(k))
                if __day_count > 5:
                    self.task_complete_button.setStyleSheet("QPushButton\
                     {background-color: #ff0000; border-radius: 10px; font: bold 14px;min-width: 3em; padding: 1px;\
                      color: white;}"
                                                            "QPushButton:pressed { background-color: #990000; "
                                                            "border-radius: 10px;"
                                                            "font: bold 14px;min-width: 3em; padding: 1px; color: white;}")
                else:
                    self.task_complete_button.setStyleSheet("QPushButton\
                     {background-color: green; border-radius: 10px; font: bold 14px;min-width: 3em; padding: 1px;\
                      color: white;}"
                                                            "QPushButton:pressed { background-color: #004d00;"
                                                            "border-radius: 10px;font: bold 14px;min-width: 3em;\
                                                     padding: 1px; color: white;}")
                self.task_complete_button.show()
                __y += __h + 20
            __y = self.SCREEN_H // 5
            __x = __x + __w + __column_space


if __name__ == '__main__':
    app = QApplication()
    assembly = Assembly()
    sys.exit(app.exec())
