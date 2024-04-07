from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from models import db, Restaurant, Pizza, RestaurantPizza


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///restaurant.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route("/")
def index():
    return "<h1>Pizza Restaurants by Felix Omondi</h1>"


@app.route("/restaurants")
def restaurants():
    restaurant_list = []
    for restaurant in Restaurant.query.all():
        restaurant_dict = {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address,
        }
        restaurant_list.append(restaurant_dict)
    return jsonify(restaurant_list)


@app.route("/restaurants/<int:id>", methods=["GET", "DELETE"])
def restaurants_by_id(id):
    restaurant = Restaurant.query.filter(Restaurant.id == id).first()
    if request.method == "GET":
        if restaurant:
            restaurant_dict = restaurant.to_dict()
            response = make_response(restaurant_dict, 200)
            return response
        else:
            message = {"error": "Restaurant not found"}
            response = make_response(message, 404)
            return response
    elif request.method == "DELETE":
        if restaurant:
            db.session.delete(restaurant)
            db.session.commit()
            response_body = {}
            response = make_response(response_body, 200)
            return response
        else:
            message = {"error": "Restaurant not found"}
            response = make_response(message, 404)
            return response


@app.route("/pizzas", methods=["GET"])
def pizzas():
    pizza_list = []
    for pizza in Pizza.query.all():
        pizza_dict = pizza.to_dict(only=["id", "ingredients", "name"])
        pizza_list.append(pizza_dict)
    response = make_response(pizza_list, 200)
    return response


@app.route("/restaurant_pizzas", methods=["POST"])
def restaurant_pizzas():
    price = request.form.get("price")
    pizza_id = request.form.get("pizza_id")
    restaurant_id = request.form.get("restaurant_id")

    # Check if all required data is provided
    if not (price and pizza_id and restaurant_id):
        message = {"errors": ["Validation errors"]}
        response = make_response(message, 400)
        return response

    # Fetch the associated Pizza object
    pizza = Pizza.query.get(pizza_id)
    if not pizza:
        message = {"errors": [f"Pizza with id {pizza_id} not found."]}
        response = make_response(message, 404)
        return response

    # Return the data related to the Pizza upon successful creation of RestaurantPizza
    pizza_data = pizza.to_dict(only=["id", "name", "ingredients"])
    return jsonify(pizza_data), 201


if __name__ == "__main__":
    app.run(debug=True)
