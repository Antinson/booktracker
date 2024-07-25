from flask import Flask, render_template, request, jsonify, redirect, url_for, Blueprint, current_app, make_response
import services
from .models import Book, Tracking

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('home.html')

@main_bp.route('/getbooks', methods=['GET'])
def get_books():
    
    page = request.args.get('page', 1, type=int)
    per_page = 10

    books = Book.query.paginate(page=page, per_page=per_page)

    books_list = [book.to_dict() for book in books.items]

    return jsonify({
        'books': books_list,
        'pages': books.pages,
        'total': books.total,
        'has_next': books.has_next,
        'has_prev': books.has_prev
    })

@main_bp.route('/addbook', methods=['GET'])
def add_book_view():
    return render_template('addbook.html')

@main_bp.route('/updatebook/<id>', methods=['GET'])
def update_book_view(id):
    return render_template('updatebook.html')


@main_bp.route('/addbook', methods=['POST'])
def add_book():
    try:
        data = request.json


        required_fields = ['title', 'pages']

        # Validation for required fields
        for field in required_fields:
            if field not in data:
                return jsonify({'message': f'Missing field: {field}'}), 400

        new_book = Book(
            title=data['title'],
            path='/books/',
            semester=data.get('semester'),
            class_name=data.get('class_name'),
            book_cover=data.get('book_cover'),
            subject=data.get('subject'),
            pages=data['pages'],
            pages_read=data.get('pages_read', 0)  # Default to 0 if not provided
        )

        db.session.add(new_book)
        db.session.commit()

        return jsonify({'message': 'Success', 'book': new_book.title})

    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Error: {str(e)}'}), 500


@main_bp.route('/updatebook/<id>', methods=['PUT'])
def update_book(id):
    pass
