import datetime

from flask.ext.sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_db(app):
    global db
    db = SQLAlchemy(app)


class BaseModel(object):
    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def rollback():
        db.session.rollback()


class GifterStats(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)

    screen_name = db.Column(db.String())
    # created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)
    created_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    gift_category = db.Column(db.String())
    interest_category = db.Column(db.String())

    def __init__(self, screen_name, gift_category, interest_category):
        self.screen_name = screen_name
        self.gift_category = gift_category
        self.interest_category = interest_category


#  TODO MOVE to Fun project when created
class FunStats(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)

    screen_name = db.Column(db.String())
    # created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)
    created_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow)

    interest_category = db.Column(db.String())

    def __init__(self, screen_name, interest_category):
        self.screen_name = screen_name
        self.interest_category = interest_category
