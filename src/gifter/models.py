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


class SearchedModel(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)

    screen_name = db.Column(db.String())
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    gift_category = db.Column(db.String())

    def __init__(self, screen_name, gift_category):
        self.screen_name = screen_name
        self.gift_category = gift_category


class PredictedModel(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)

    screen_name = db.Column(db.String())
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    predicted_category = db.Column(db.String())

    def __init__(self, screen_name, predicted_category):
        self.screen_name = screen_name
        self.predicted_category = predicted_category


class CounterModel(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)

    url = db.Column(db.String)
    counter = db.Column(db.Integer, default=0)
    category_name = db.Column(db.String)
    item_title = db.Column(db.String)
