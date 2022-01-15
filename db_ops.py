from peewee import *

db = SqliteDatabase("tasks.db")


class Monday(Model):
    monday = CharField()

    class Meta:
        database = db
        db_table = "Monday"


class Tuesday(Model):
    tuesday = CharField()

    class Meta:
        database = db
        db_table = "Tuesday"


class Wednesday(Model):
    wednesday = CharField()

    class Meta:
        database = db
        db_table = "Wednesday"


class Thursday(Model):
    thursday = CharField()

    class Meta:
        database = db
        db_table = "Thursday"


class Friday(Model):
    friday = CharField()

    class Meta:
        database = db
        db_table = "Friday"


class Saturday(Model):
    saturday = CharField()

    class Meta:
        database = db
        db_table = "Saturday"


class Sunday(Model):
    sunday = CharField()

    class Meta:
        database = db
        db_table = "Sunday"


with db:
    db.create_tables([Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday])


def monday_add_task(task_obj, time, task):
    local_task = task_obj(time, task).task_text
    with db:
        Monday.insert(monday=local_task).execute()


def tuesday_add_task(task_obj, time, task):
    local_task = task_obj(time, task).task_text
    with db:
        Tuesday.insert(tuesday=local_task).execute()


def wednesday_add_task(task_obj, time, task):
    local_task = task_obj(time, task).task_text
    with db:
        Wednesday.insert(wednesday=local_task).execute()


def thursday_add_task(task_obj, time, task):
    local_task = task_obj(time, task).task_text
    with db:
        Thursday.insert(thursday=local_task).execute()


def friday_add_task(task_obj, time, task):
    local_task = task_obj(time, task).task_text
    with db:
        Friday.insert(friday=local_task).execute()


def saturday_add_task(task_obj, time, task):
    local_task = task_obj(time, task).task_text
    with db:
        Saturday.insert(saturday=local_task).execute()


def sunday_add_task(task_obj, time, task):
    local_task = task_obj(time, task).task_text
    with db:
        Sunday.insert(sunday=local_task).execute()


def remove_task(day_obj, full_task_text):
    with db:
        day_obj.delete().where(task=full_task_text).execute()


'''def fill_tasks(day_obj, day_column):
    day_obj.tasks.clear()
    with db:
        for k in WeekDB.select(WeekDB.day_column):
            day_obj.tasks.append(k)'''
