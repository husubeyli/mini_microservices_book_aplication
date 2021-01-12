from book_service.config.extentions import ma
from marshmallow import fields
from book_service.models import Book
from marshmallow_sqlalchemy import ModelSchema, auto_field


class BookSchema(ma.SQLAlchemyAutoSchema):

    price = auto_field()
    pudblished_at = auto_field()
    title = auto_field()
    author = auto_field()
    
    class Meta:
        model = Book
        # include_fk = True
        load_instance = True
