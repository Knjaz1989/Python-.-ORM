from sqlalchemy import Column, Integer, Text, Date, Float, ForeignKey
from db import Base, engine


class Publisher(Base):
    __tablename__ = 'publisher'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(Text)
    publisher_id = Column(Integer, ForeignKey(Publisher.id))


class Shop(Base):
    __tablename__ = 'shop'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text)


class Stock(Base):
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey(Book.id))
    shop_id = Column(Integer, ForeignKey(Shop.id))
    count = Column(Integer)


class Sale(Base):
    __tablename__ = 'sale'

    id = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(Float)
    date_sale = Column(Date)
    count = Column(Integer)
    stock_id = Column(Integer, ForeignKey(Stock.id))


if __name__ == '__main__':
    Base.metadata.create_all(engine)
