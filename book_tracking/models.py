from book_tracking import db
from datetime import datetime

class Book(db.Model):

    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    path = db.Column(db.String(80), nullable=False)
    semester = db.Column(db.String(12), nullable=True)
    class_name = db.Column(db.String(80), nullable=True)
    book_cover = db.Column(db.String(80), nullable=True)
    subject = db.Column(db.String(80), nullable=True)
    pages = db.Column(db.Integer, nullable=False)
    pages_read = db.Column(db.Integer, nullable=True, default=0)

    trackings = db.relationship('Tracking', back_populates='book', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'path': self.path,
            'semester': self.semester,
            'class_name': self.class_name,
            'book_cover': self.book_cover,
            'subject': self.subject,
            'pages': self.pages,
            'pages_read': self.pages_read,
            'trackings': [tracking.to_dict() for tracking in self.trackings]
        }


class Tracking(db.Model):

    __tablename__ = 'trackings'

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    pages_read = db.Column(db.Integer, nullable=True, default=0)

    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)

    book = db.relationship('Book', back_populates='trackings')

    def to_dict(self):
        return {
            'id': self.id,
            'timestamp': self.timestamp.isoformat(),
            'pages_read': self.pages_read,
            'book_id': self.book_id
        }

