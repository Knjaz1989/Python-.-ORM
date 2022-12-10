import json

from db import db as db_session
from models import Publisher, Shop, Book, Stock, Sale


def insert_data():
    with open('fixtures/tests_data_1.json', 'r') as file:
        data = json.load(file)

    for record in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[record.get('model')]
        db_session.add(model(id=record.get('pk'), **record.get('fields')))
        db_session.commit()


if __name__ == '__main__':
    insert_data()
