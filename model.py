from peewee import *
import datetime

db = SqliteDatabase('adminfest.db')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    """
    ORM model of the User table
    """
    #username = CharField(unique=True)
    user_id = TextField(unique=True)


class BeerCode(BaseModel):
    """
    ORM model of the BeerCode table
    """
    beer_code = TextField()
    user = ForeignKeyField(User, related_name='users')
    timestamp = DateTimeField()


class Tweet(BaseModel):
    """
    ORM model of the Tweet table
    """
    user = ForeignKeyField(User, related_name='tweets')
    status_id = TextField(unique=True)
    message = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)
    is_published = BooleanField(default=True)


if __name__ == "__main__":
    try:
        User.create_table()
    except OperationalError:
        print("User table already exists!")

    try:
        BeerCode.create_table()
    except OperationalError:
        print("BeerCode table already exists!")

    try:
        Tweet.create_table()
    except OperationalError:
        print("Tweet table already exists!")

