from models import *
import json

from config import db


def insert_data_user(input_data):
    """Adds user data to database"""

    for row in input_data:
        db.session.add(
            User(**row))
    db.session.commit()


def insert_data_order(input_data):
    """Adds order data to database"""

    for row in input_data:
        db.session.add(Order(**row))
    db.session.commit()


def insert_data_offer(input_data):
    """Adds offer data to database"""

    for row in input_data:
        db.session.add(
            Offer(**row))
    db.session.commit()


# For users

def get_all_data(model):
    """Returns all data as JSON for requested class """
    result = []
    for row in db.session.query(model).all():
        result.append(row.to_dict())
    return result


def get_data_by_id(model, data_id):
    """Returns data as JSON for requested class and requested ID"""
    try:
        return db.session.query(model).filter(model.id == data_id).all()[0].to_dict()
    except Exception:
        return {}


def add_universal(model, values):
    """Adds data to database when no ID identified, ID assigned by autoincrement"""
    try:
        for row in values:
            db.session.add(model(**row))
            db.session.commit()
    except Exception:
        return {}


def update_universal(model, user_id, values):
    """Replaces data in database with values defined in input JSON"""
    try:
        data = db.session.query(model).filter(model.id == user_id).update(values)
        data.update().values(values)
        db.session.commit()
    except Exception:
        return {}


def delete_universal(model, user_id):
    """Deletes data with requested ID"""
    try:
        data = db.session.query(model).get(user_id)
        db.session.delete(data)
        db.session.commit()
    except Exception:
        return {}


def init_db():
    db.drop_all()
    db.create_all()
    with open("data/users.json", encoding="utf-8") as file:
        insert_data_user(json.load(file))

    with open("data/orders.json", encoding="utf-8") as file:
        insert_data_order(json.load(file))

    with open("data/offers.json", encoding="utf-8") as file:
        insert_data_offer(json.load(file))
