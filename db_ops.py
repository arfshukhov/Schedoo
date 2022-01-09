from peewee import *

db = SqliteDatabase("tasks.db")


class DayTask(Model):
    task = TextField()

    class Meta:
        database = db


class Monday(DayTask):
    class Meta:
        db_table = "monday"


class Tuesday(DayTask):
    class Meta:
        db_table = "tuesday"


class Wednesday(DayTask):
    class Meta:
        db_table = "wednesday"


class Thursday(DayTask):
    class Meta:
        db_table = "thursday"


class Friday(DayTask):
    class Meta:
        db_table = "friday"


class Saturday(DayTask):
    class Meta:
        db_table = "saturday"


class Sunday(DayTask):
    class Meta:
        db_table = "sunday"


with db:
    db.create_tables([Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday])
