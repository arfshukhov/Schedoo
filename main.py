# import schedule
import time
from threading import Thread
import __future__
from db_ops import *
import asyncio

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from functools import partial

import sys

from win32api import GetSystemMetrics

SCREEN_W = GetSystemMetrics(0) // 1.2
SCREEN_H = GetSystemMetrics(1) // 1.8


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


class AddTaskWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setStyleSheet("background-color: #293133")
        self.add_task_screen_w = SCREEN_W // 2.5
        self.add_task_screen_h = SCREEN_H * 1.2
        self.setGeometry(300, 300, self.add_task_screen_w, self.add_task_screen_h)
        self.show()



        self.__w = SCREEN_W // 8.5
        self.__h = SCREEN_H // 28


        self.hours_space = QLineEdit(self)
        self.hours_space.setStyleSheet("background-color: gray; border-radius: 10px; min-width: 3em; color:\
                white; selection-color: yellow; selection-background-color: blue;")
        self.hours_space.setFont(QFont("Bold", SCREEN_H // 25))
        self.hours_space.setGeometry(SCREEN_W // 62, SCREEN_H // 48, 90, 50)
        hIntValidator = QIntValidator(self)
        hIntValidator.setRange(0, 23)
        self.hours_space.setValidator(hIntValidator)
        self.hours_space.setInputMask("HH:HH")
        self.hours_space.setMaxLength(4)
        self.hours_space.setAlignment(Qt.AlignCenter)
        self.hours_space.setText("0000")
        self.hours_space.show()

        '''self.minutes_space = QLineEdit(self)
        self.minutes_space.setStyleSheet("background-color: gray; border-radius: 10px; min-width: 3em; color:\
                        white; selection-color: yellow; selection-background-color: blue;")
        self.minutes_space.setFont(QFont("Bold", SCREEN_H // 25))
        self.minutes_space.setGeometry(SCREEN_W // 17, SCREEN_H // 48, 50, 50)
        self.minutes_space.setMaxLength(2)
        mIntValidator = QIntValidator(self)
        mIntValidator.setRange(0, 59)
        self.minutes_space.setValidator(mIntValidator)
        self.minutes_space.setAlignment(Qt.AlignCenter)
        self.minutes_space.setText(str(self.hours_value))
        self.minutes_space.show()'''

        self.text_space = QTextEdit(self)
        self.text_space.setStyleSheet("background-color: gray; border-radius: 10px; min-width: 3em; color:\
                                white; selection-color: yellow; selection-background-color: blue;")
        self.text_space.setFont(QFont("Bold", SCREEN_H // 40))
        self.text_space.palette().setColor(QPalette.Base, Qt.black)
        self.text_space.setGeometry(SCREEN_W // 62, SCREEN_H // 8.5, SCREEN_W//6, SCREEN_H // 6)
        self.text_space.textChanged.connect(self.control_text_length)
        self.text_space.setAlignment((Qt.AlignLeft | Qt.AlignTop))
        self.text_space.setWordWrapMode(QTextOption.WrapAtWordBoundaryOrAnywhere)
        self.text_space.show()

        self.upper_button = QPushButton(self)
        self.upper_button.setStyleSheet(self.set_style_sheet("blue", "green"))
        self.upper_button.setGeometry(200, 150, 25, 25)
        self.upper_button.setText("Done!")
        self.upper_button.show()

    def choice_day_button(self, day_name):
        button = QPushButton(self)

    def control_text_length(self):
        text = self.text_space.toPlainText()

        if len(text) >= 80:
            self.text_space.setText(text[0: 80])
        else:
            pass


    @staticmethod
    def set_style_sheet(bg_color, pressed_color) -> str:
        style_sheet_preset = "".join(["QPushButton{background-color:", bg_color, "; border-radius: 10px; font: bold 14px;min-width: 3em;\
                padding: 1px; color: white;} QPushButton:pressed { background-color:", pressed_color, ";\
                border-radius: 10px;font: bold 14px;min-width: 3em; padding: 1px; color: white;}"])
        return style_sheet_preset

    def draw_add_tasks_button(self, x, y, is_holyday: bool):
        add_task_button_monday = QPushButton(self)
        add_task_button_monday.setGeometry(x, y, self.__w * 0.8, self.__h)
        add_task_button_monday.setText("Add new task")

        if is_holyday:
            bg_color, pressed_color = "#ff0000", "#990000"
        else:
            bg_color, pressed_color = "green", "#004d00"

        add_task_button_monday.setStyleSheet(self.set_style_sheet(bg_color, pressed_color))
        add_task_button_monday.show()



    def draw(self):
        ...
        #self.draw_add_tasks_monday(SCREEN_W // 85, False)
        #self.draw_add_tasks_tuesday(SCREEN_W // 4.5, False)'''


class Assembly(QWidget):
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
                          color: white;} QPushButton:pressed { background-color: #990000; border-radius: 10px;\
                                                    font: bold 14px;min-width: 3em; padding: 1px; color: white;}"
                                                   "QPushButton:pressed { background-color: #6600ff; border-radius: 10px;\
                                                    font: bold 14px;min-width: 3em; padding: 1px; color: white;}")
        self.set_default_size_button.show()

        self.add_task_button = QPushButton(self)
        self.add_task_button.setText("Add Task")
        self.add_task_button.setGeometry(SCREEN_W * 0.725, 7, SCREEN_W // 9, SCREEN_H // 20)
        self.add_task_button.setStyleSheet("QPushButton\
                                 {background-color: #8b00ff; border-radius: 10px; font: bold 14px;min-width: 3em; padding: 1px;\
                                  color: white;} QPushButton:pressed { background-color: #990000; border-radius: 10px;\
                                                            font: bold 14px;min-width: 3em; padding: 1px; color: white;}"
                                           "QPushButton:pressed { background-color: #6600ff; border-radius: 10px;\
                                                    font: bold 14px;min-width: 3em; padding: 1px; color: white;}")
        self.add_task_button.clicked.connect(partial(self.draw_add_task_window))
        self.week = Week()
        self.show()
        self.widget: object
        self.day_column: object
        self.task_column: object
        self.complete_button: object
        self.cancel_button: object
        self.draw_columns()
        self.draw_day_names()
        self.draw_tasks()

        self.add_task_window = AddTaskWindow()

    def draw_add_task_window(self):
        self.add_task_window.show()

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
    app = QApplication(sys.argv)
    assembly = AddTaskWindow()
    app.exec()
