from book_service.config.extentions import db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.sql import func


class SaveMixin(object):
    id = db.Column(db.Integer, primary_key=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Book(SaveMixin, db.Model):
    #informations
    # id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    pudblished_at = db.Column(db.Integer, nullable=False)

    #modertaion's
    is_published = db.Column(db.Boolean(), default=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), server_onupdate=func.now(), nullable=False)

    def __init__(self, title, author, price, pudblished_at, is_published=True):
        self.title = title
        self.author = author
        self.__price = price
        self.pudblished_at = pudblished_at


    # @property
    # def price(self):
    #     return f'{self.price}'

    # @price.setter
    # def price(self, new_price):
    #     self.price = new_price


    def __repr__(self):
        return self.title

