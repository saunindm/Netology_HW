import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import json
import os

PG_LOGIN = os.getenv("PG_LOGIN")
PG_PASS = os.getenv("PG_PASS")
DB_NAME = os.getenv("DB_NAME")

Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=100), unique=True)


class Shop(Base):
    __tablename__ = 'shop'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=100), unique=True)


class Book(Base):
    __tablename__ = 'book'
    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=100), unique=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'))

    publisher = relationship(Publisher, backref='book')


class Stock(Base):
    __tablename__ = 'stock'
    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'), nullable=False)
    count = sq.Column(sq.Integer)

    book = relationship(Book, backref='stock')
    shop = relationship(Shop, backref='stock')


class Sale(Base):
    __tablename__ = 'sale'
    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Float)
    date_sale = sq.Column(sq.Date)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'), nullable=False)
    count = sq.Column(sq.Integer)

    stock = relationship(Stock, backref='sale')


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    engine = sq.create_engine(f'postgresql://{PG_LOGIN}:{PG_PASS}@localhost:5432/{DB_NAME}')
    con = engine.connect()
    create_tables(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    with open('data.json', 'r') as fd:
        data = json.load(fd)

    for record in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[record.get('model')]
        session.add(model(id=record.get('pk'), **record.get('fields')))
    session.commit()

    res = input('Введите id издателя: ')
    query_1 = session.query(Publisher).filter(Publisher.id == res)  # вывод издателя (publisher), имя или идентификатор которого принимается через input().
    query_2 = session.query(Shop).join(Stock.shop).join(Stock.book).join(Book.publisher).filter(Publisher.id == res)  # запрос выборки магазинов, продающих целевого издателя.
    for i in query_1.all():
        print(f'{res} - {i.name}')
    print("Магазины, продающие данного издателя:")
    for i in query_2.all():
        print(f'{res} - {i.name}')

    session.close()
    con.close()
