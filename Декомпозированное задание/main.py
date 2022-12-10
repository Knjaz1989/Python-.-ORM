from db import db as db_session
from models import Publisher


def get_publisher(data):
    item = db_session.query(Publisher).filter(Publisher.name == data).first()
    if not item and data.isdigit():
        item = db_session.query(Publisher).get(data)
    elif not item:
        return "Такого публициста нет"
    return item


if __name__ == '__main__':
    input_data = input("Введите id публициста или его имя: ")
    print(get_publisher(input_data))
