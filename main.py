import json

from flask import request

from config import app
from models import User, Order, Offer
from service import init_db, update_universal, add_universal, delete_universal, get_all_data, get_data_by_id


# For users

@app.route("/users/", methods=["GET", "POST"])
def actions_users():
    if request.method == "GET":
        return app.response_class(
            response=json.dumps(get_all_data(User)),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "POST":
        if isinstance(request.json, list):
            add_universal(User, request.json)
        elif isinstance(request.json, dict):
            add_universal(User, [request.json])
        else:
            print("Wrong data type")
        return app.response_class(
            response=json.dumps(request.json, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/users/<int:user_id>", methods=["GET", "PUT", "DELETE"])
def actions_user_by_id(user_id):
    if request.method == "GET":
        data = get_data_by_id(User, user_id)
        return app.response_class(
            response=json.dumps(data, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "PUT":
        update_universal(User, user_id, request.json)
        return app.response_class(
            response=json.dumps(["OK"], ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "DELETE":
        delete_universal(User, user_id)
        return app.response_class(
            response=json.dumps(["Record removed"], ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


# For orders

@app.route("/orders/", methods=["GET", "POST"])
def action_orders():
    if request.method == "GET":
        return app.response_class(
            response=json.dumps(get_all_data(Order)),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "POST":
        if isinstance(request.json, list):
            add_universal(Order, request.json)
        elif isinstance(request.json, dict):
            add_universal(Order, [request.json])
        else:
            print("Wrong data type")
        return app.response_class(
            response=json.dumps(request.json, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/orders/<int:order_id>", methods=["GET", "PUT", "DELETE"])
def actions_order_by_id(order_id):
    if request.method == "GET":
        data = get_data_by_id(Order, order_id)
        return app.response_class(
            response=json.dumps(data, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "PUT":
        update_universal(Order, order_id, request.json)
        return app.response_class(
            response=json.dumps(["OK"], ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "DELETE":
        delete_universal(Order, order_id)
        return app.response_class(
            response=json.dumps(["Record removed"], ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


# For offers

@app.route("/offers/", methods=["GET", "POST"])
def action_offers():
    if request.method == "GET":
        return app.response_class(
            response=json.dumps(get_all_data(Offer)),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "POST":
        if isinstance(request.json, list):
            add_universal(Offer, request.json)
        elif isinstance(request.json, dict):
            add_universal(Offer, [request.json])
        else:
            print("Wrong data type")
        return app.response_class(
            response=json.dumps(request.json, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/offers/<int:offer_id>", methods=["GET", "PUT", "DELETE"])
def actions_offer_by_id(offer_id):
    if request.method == "GET":
        data = get_data_by_id(Offer, offer_id)
        return app.response_class(
            response=json.dumps(data, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "PUT":
        update_universal(Offer, offer_id, request.json)
        return app.response_class(
            response=json.dumps(["OK"], ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "DELETE":
        delete_universal(Offer, offer_id)
        return app.response_class(
            response=json.dumps(["Record removed"], ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


if __name__ == '__main__':
    init_db()
    app.run(host="0.0.0.0", port=8000, debug=True)
