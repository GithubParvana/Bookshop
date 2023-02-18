# butun databse elaqelerimiz burda bas verecek;

from extensions import db
from app import app


# SQLAlchemy'ye uygun table'lar yaradiriq;

class Book(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    author = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float())
    img_url = db.Column(db.String(255), index=True)
    description = db.Column(db.String(255), nullable=False)
    stock = db.Column(db.Integer())
    publisher = db.Column(db.String(255))
    lang_id = db.Column(db.Integer(), db.ForeignKey('language.id'), nullable=False)
    genre_id = db.Column(db.Integer(), db.ForeignKey('genre.id'), nullable=False)

    


    def __init__(self, name, author, price, img_url, description, stock, publisher, lang_id, genre_id):
        self.name = name
        self.author = author
        self.price = price
        self.img_url = img_url
        self.description = description
        self.stock = stock
        self.genre_id = genre_id
        self.lang_id = lang_id
        self.publisher = publisher


    
    def __repr__(self):
        return self.name



    def save(self):
        db.session.add(self)
        db.session.commit()






class Genre(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    genre = db.Column(db.String(255))




    def __init__(self, genre):
        self.genre = genre
    


    def __repr__(self):
        return self.genre



    def save(self):
        db.session.add(self)
        db.session.commit()




class Language(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    language = db.Column(db.String(255))

    

    def __init__(self, language):
        self.language = language
    


    def __repr__(self):
        return self.language



    def save(self):
        db.session.add(self)
        db.session.commit()