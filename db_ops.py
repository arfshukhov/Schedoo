from peewee import *


db = SqliteDatabase("tasks.db")


class WeekDB(Model):
    monday = CharField()
    tuesday = CharField()
    wednesday = CharField()
    thursday = CharField()
    friday = CharField()
    saturday = CharField()
    sunday = CharField()

    class Meta:
        database = db


with db:
    db.create_tables([WeekDB])


class Task:
    def __init__(self, time, task_text):
        self.task_text: str = " - ".join([time, task_text])


def add_task(time, task, day_name):
    local_task1 = Task(time, task).task_text
    WeekDB.insert(
        {day_name: local_task1}
    ).execute()

