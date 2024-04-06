from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Restaurant, Pizza, RestaurantPizza


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///restaurant.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


# @app.route("/")
# def index():
#     return "<h1>Pizza Restaurants</h1>"


# @app.route("/restaurants")
# def restaurants():
#     pass


# @app.route("/restaurants/<Integer:id>", methods=["GET", "DELETE"])
# def restaurants_by_id(id):
#     pass


# @app.route("/pizzas", methods=["GET", "POST"])
# def pizzas():
#     pass


if __name__ == "__main__":
    app.run(debug=True)
