# import schedule
# import time
from threading import Thread
from db_ops import *

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import sys

from win32api import GetSystemMetrics

SCREEN_W = GetSystemMetrics(0) // 1.2
SCREEN_H = GetSystemMetrics(1) // 1.8


class Task:
    def __init__(self, time, task_text):
        self.task_text: str = " - ".join([time, task_text])

    def __str__(self):
        return self.task_text


class Day:
    tasks = []

    def __init__(self, day_name):
        self.day_name = day_name
        self.tasks: list = []


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

# Да, в этом фрагменте кода я положил огромный болт на принцип DRY,
# но это было единственным решением проблемы с работой базы данных.
# Возможно, потом найду способ реализовать через объект класса
# Yes, in this code snippet I put a huge dick on the DRY principle,
# but this was the only solution to the problem with the database operation.
# I'll find a way to implement it through a class object.


class AddTaskButtons(QWidget):
    def __init__(self):
        super().__init__()

    def draw_add_tasks_monday(self, __x, is_holyday: bool):
        __x = __x
        __y = SCREEN_H // 8
        __w = SCREEN_W // 8.5
        __h = SCREEN_H // 28
        __column_space = SCREEN_W // 41
        add_task_button_monday = QPushButton(self)
        add_task_button_monday.setGeometry(__x + __w // 9, __y, __w * 0.8, __h)
        add_task_button_monday.setText("Add new task")

        if is_holyday:
            bg_color, pressed_color = "#ff0000", "#990000"
        else:
            bg_color, pressed_color = "green", "#004d00"

        add_task_button_monday.setStyleSheet(
            "".join(["QPushButton{background-color:", bg_color, "; border-radius: 10px; font: bold 14px;min-width: 3em;\
                padding: 1px; color: white;} QPushButton:pressed { background-color:", pressed_color, ";\
                border-radius: 10px;font: bold 14px;min-width: 3em; padding: 1px; color: white;}"]))
        add_task_button_monday.clicked.connect(monday_add_task(Task, "10:00", "its monday"))
        add_task_button_monday.clicked.connect(self.draw)
        add_task_button_monday.show()

    def draw_add_tasks_tuesday(self, __x, is_holyday: bool):
        __x = __x
        __y = SCREEN_H // 8
        __w = SCREEN_W // 8.5
        __h = SCREEN_H // 28
        __column_space = SCREEN_W // 41
        add_task_button_tuesday = QPushButton(self)
        add_task_button_tuesday.setGeometry(__x + __w // 9, __y, __w * 0.8, __h)
        add_task_button_tuesday.setText("Add new task")

        if is_holyday:
            bg_color, pressed_color = "#ff0000", "#990000"
        else:
            bg_color, pressed_color = "green", "#004d00"

        add_task_button_tuesday.setStyleSheet(
            "".join(["QPushButton{background-color:", bg_color, "; border-radius: 10px; font: bold 14px;min-width: 3em;\
                padding: 1px; color: white;} QPushButton:pressed { background-color:", pressed_color, ";\
                border-radius: 10px;font: bold 14px;min-width: 3em; padding: 1px; color: white;}"]))
        add_task_button_tuesday.clicked.connect(tuesday_add_task(Task, "15:34", "its wednesday"))
        add_task_button_tuesday.clicked.connect(self.draw)
        add_task_button_tuesday.show()

    def draw_add_tasks_wednesday(self, __x, is_holyday: bool):
        __x = __x
        __y = SCREEN_H // 8
        __w = SCREEN_W // 8.5
        __h = SCREEN_H // 28
        __column_space = SCREEN_W // 41
        add_task_button_wednesday = QPushButton(self)
        add_task_button_wednesday.setGeometry(__x + __w // 9, __y, __w * 0.8, __h)
        add_task_button_wednesday.setText("Add new task")

        if is_holyday:
            bg_color, pressed_color = "#ff0000", "#990000"
        else:
            bg_color, pressed_color = "green", "#004d00"

        add_task_button_wednesday.setStyleSheet(
            "".join(["QPushButton{background-color:", bg_color, "; border-radius: 10px; font: bold 14px;min-width: 3em;\
                padding: 1px; color: white;} QPushButton:pressed { background-color:", pressed_color, ";\
                border-radius: 10px;font: bold 14px;min-width: 3em; padding: 1px; color: white;}"]))
        add_task_button_wednesday.clicked.connect(Task, "16:40", "its wednesday")
        add_task_button_wednesday.clicked.connect(self.draw)
        add_task_button_wednesday.show()

    def draw_add_tasks_thursday(self, __x, is_holyday: bool):
        __x = __x
        __y = SCREEN_H // 8
        __w = SCREEN_W // 8.5
        __h = SCREEN_H // 28
        __column_space = SCREEN_W // 41
        add_task_button_thursday = QPushButton(self)
        add_task_button_thursday.setGeometry(__x + __w // 9, __y, __w * 0.8, __h)
        add_task_button_thursday.setText("Add new task")

        if is_holyday:
            bg_color, pressed_color = "#ff0000", "#990000"
        else:
            bg_color, pressed_color = "green", "#004d00"

        add_task_button_thursday.setStyleSheet(
            "".join(["QPushButton{background-color:", bg_color, "; border-radius: 10px; font: bold 14px;min-width: 3em;\
                padding: 1px; color: white;} QPushButton:pressed { background-color:", pressed_color, ";\
                border-radius: 10px;font: bold 14px;min-width: 3em; padding: 1px; color: white;}"]))
        add_task_button_thursday.clicked.connect(Task, "17:57", "its thursday")
        add_task_button_thursday.clicked.connect(self.draw)
        add_task_button_thursday.show()

    def draw_add_tasks_friday(self, __x, is_holyday: bool):
        __x = __x
        __y = SCREEN_H // 8
        __w = SCREEN_W // 8.5
        __h = SCREEN_H // 28
        __column_space = SCREEN_W // 41
        add_task_button_friday = QPushButton(self)
        add_task_button_friday.setGeometry(__x + __w // 9, __y, __w * 0.8, __h)
        add_task_button_friday.setText("Add new task")

        if is_holyday:
            bg_color, pressed_color = "#ff0000", "#990000"
        else:
            bg_color, pressed_color = "green", "#004d00"

        add_task_button_friday.setStyleSheet(
            "".join(["QPushButton{background-color:", bg_color, "; border-radius: 10px; font: bold 14px;min-width: 3em;\
                padding: 1px; color: white;} QPushButton:pressed { background-color:", pressed_color, ";\
                border-radius: 10px;font: bold 14px;min-width: 3em; padding: 1px; color: white;}"]))
        add_task_button_friday.clicked.connect(Task, "18:40", "its friday")
        add_task_button_friday.clicked.connect(self.draw)
        add_task_button_friday.show()

    def draw_add_tasks_saturday(self, __x, is_holyday: bool, add_task_func):
        __x = __x
        __y = SCREEN_H // 8
        __w = SCREEN_W // 8.5
        __h = SCREEN_H // 28
        __column_space = SCREEN_W // 41
        add_task_button_saturday = QPushButton(self)
        add_task_button_saturday.setGeometry(__x + __w // 9, __y, __w * 0.8, __h)
        add_task_button_saturday.setText("Add new task")

        if is_holyday:
            bg_color, pressed_color = "#ff0000", "#990000"
        else:
            bg_color, pressed_color = "green", "#004d00"

        add_task_button_saturday.setStyleSheet(
            "".join(["QPushButton{background-color:", bg_color, "; border-radius: 10px; font: bold 14px;min-width: 3em;\
                padding: 1px; color: white;} QPushButton:pressed { background-color:", pressed_color, ";\
                border-radius: 10px;font: bold 14px;min-width: 3em; padding: 1px; color: white;}"]))
        add_task_button_saturday.clicked.connect(Task, "20:20", "its saturday")
        add_task_button_saturday.clicked.connect(self.draw)
        add_task_button_saturday.show()

    def draw_add_tasks_sunday(self, __x, is_holyday: bool):
        __x = __x
        __y = SCREEN_H // 8
        __w = SCREEN_W // 8.5
        __h = SCREEN_H // 28
        __column_space = SCREEN_W // 41
        add_task_button_sunday = QPushButton(self)
        add_task_button_sunday.setGeometry(__x + __w // 9, __y, __w * 0.8, __h)
        add_task_button_sunday.setText("Add new task")

        if is_holyday:
            bg_color, pressed_color = "#ff0000", "#990000"
        else:
            bg_color, pressed_color = "green", "#004d00"

        add_task_button_sunday.setStyleSheet(
            "".join(["QPushButton{background-color:", bg_color, "; border-radius: 10px; font: bold 14px;min-width: 3em;\
                padding: 1px; color: white;} QPushButton:pressed { background-color:", pressed_color, ";\
                border-radius: 10px;font: bold 14px;min-width: 3em; padding: 1px; color: white;}"]))
        add_task_button_sunday.clicked.connect(sunday_add_task(Task, "21:00", "its sunday"))
        add_task_button_sunday.clicked.connect(self.draw)
        add_task_button_sunday.show()

    def draw(self):
        self.draw_add_tasks_monday(SCREEN_W//85, False)
        self.draw_add_tasks_tuesday(SCREEN_W//4.5, False)


class Assembly(AddTaskButtons):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #293133")
        self.setGeometry(300, 300, SCREEN_W, SCREEN_H)

        self.set_default_size_button = QPushButton(self)
        self.set_default_size_button.clicked.connect(self.set_default_size)
        self.set_default_size_button.setText("Set Default Size")
        self.set_default_size_button.setGeometry(SCREEN_W * 0.865, 7, SCREEN_W // 9, SCREEN_H // 20)
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

        self.week = Week()
        '''fill_tasks(self.week.monday, WeekDB.monday)
        fill_tasks(self.week.tuesday, WeekDB.tuesday)
        fill_tasks(self.week.wednesday, WeekDB.wednesday)
        fill_tasks(self.week.thursday, WeekDB.thursday)
        fill_tasks(self.week.friday, WeekDB.friday)
        fill_tasks(self.week.saturday, WeekDB.saturday)
        fill_tasks(self.week.sunday, WeekDB.sunday)'''
        self.show()
        self.widget: object
        self.day_column: object
        self.task_column: object
        self.complete_button: object
        self.cancel_button: object
        self.draw_columns()
        self.draw()
        self.draw_day_names()
        self.draw_tasks()

    def set_default_size(self):
        self.resize(SCREEN_W, SCREEN_H)

    def draw_columns(self):
        column_list = Week()
        __x = SCREEN_W // 160
        __y = SCREEN_H // 15
        __w = SCREEN_W // 7.8
        __h = SCREEN_H * 4
        __column_space = SCREEN_W // 70
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
        __x = SCREEN_W // 85
        __y = SCREEN_H // 13
        __w = SCREEN_W // 8.5
        __h = SCREEN_H // 28
        __column_space = SCREEN_W // 41
        __day_count = 1
        for i in self.week.days_list:
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

    def draw_tasks(self):
        __x = SCREEN_W // 85
        __y = SCREEN_H // 5
        __w = SCREEN_W // 8.5
        __h = SCREEN_H // 14
        __column_space = SCREEN_W // 41
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
            __y = SCREEN_H // 5
            __x = __x + __w + __column_space


if __name__ == '__main__':
    app = QApplication()
    assembly = Assembly()
    sys.exit(app.exec())

