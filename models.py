from peewee import SqliteDatabase, TextField, DoubleField, Model

db = SqliteDatabase('albums.db')


class BaseModel(Model):
    class Meta:
        database = db


class Reviews(BaseModel):
    uri = TextField()
    score = DoubleField()
    genre = TextField()
    title = TextField()
    artist = TextField()
    album = TextField()


if __name__ == "__main__":
    db.connect()
    db.create_tables([Reviews])
    db.close()
