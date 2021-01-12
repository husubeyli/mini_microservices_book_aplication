from flask import request, jsonify, send_from_directory 
from http import HTTPStatus
from book_service.app import app
from marshmallow.exceptions import ValidationError
# from django.shortcuts import get_object_or_404

from book_service.schemas.schemas import BookSchema
from book_service.models import Book



#adding a book
@app.route('/books/', methods=['POST'])
def add_book():
    if request.method == 'POST':
        try:
            data = request.json or request.form
            serializer = BookSchema()
            print(data)
            book = serializer.load(data)
            book.save()
            return BookSchema().jsonify(book), HTTPStatus.CREATED
        except ValidationError as err:
            return jsonify(err.messages), HTTPStatus.BAD_REQUEST
    # books = Book.query.filter_by(is_published=True)
    # return BookSchema(many=True).jsonify(books), HTTPStatus.OK


#getting books
@app.route('/books/', methods=['GET'])
def all_books():
    books = Book.query.filter_by(is_published=True)
    return BookSchema(many=True).jsonify(books), HTTPStatus.OK

#getting particular book
@app.route('/book/<int:book_id>/', methods=['GET'])
def show_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return {'status': HTTPStatus.NOT_FOUND, 'description': 'Book not founded'} 
    return BookSchema().jsonify(book), HTTPStatus.OK

# #updating book
@app.route('/book/<int:book_id>/', methods=['PATCH'])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    if request.method == "PATCH":
        data = request.json or request.form
        price = data['price']
        book.price = price
        book.save()
    return BookSchema().jsonify(book), HTTPStatus.CREATED



#deleting post
@app.route('/book/<int:book_id>/', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.filter_by(id=book_id).first()
    
    if not book:
        return {'status': HTTPStatus.NOT_FOUND, 'description': 'Book not founded'}
    book.delete()
    return {'status': HTTPStatus.OK, 'description': 'Deleted successfully!'}
