from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)


# Models
class Restaurant(db.Model, SerializerMixin):
    __tablename__ = "restaurants"
    serialize_rules = ("-restaurantpizza.restaurant",)

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String)
    name = db.Column(db.String(50), unique=True)
    restaurantpizza = db.relationship("RestaurantPizza", back_populates="restaurant")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "pizzas": [
                {
                    "id": rp.pizza.id,
                    "name": rp.pizza.name,
                    "ingredients": rp.pizza.ingredients,
                }
                for rp in self.restaurantpizza
            ],
        }

    def __repr__(self):
        return f"<Restaurant {self.id}, {self.name}, {self.address}>"


class Pizza(db.Model, SerializerMixin):
    __tablename__ = "pizzas"
    serialize_rules = ("-restaurantpizza.pizza",)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    ingredients = db.Column(db.String)

    @validates("name")
    def validate_name(self, key, name):
        if len(name.strip()) == 0:
            raise ValueError("Restaurant name cannot be empty.")
        if len(name.split()) > 50:
            raise ValueError("Restaurant name must be less than 50 words.")
        return name

    # Defines relationship with RestaurantPizza
    restaurantpizza = db.relationship("RestaurantPizza", back_populates="pizza")

    def __repr__(self):
        return f"<Pizza {self.id}, {self.name}, {self.ingredients}>"


class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = "restaurantpizza"
    serialize_rules = ("-restaurant.restaurantpizza", "-pizza.restaurantpizza")
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)

    @validates("price")
    def validate_price(self, key, price):
        if price is not None and (price < 1 or price > 30):
            raise ValueError("Price must be between 1 and 30.")
        return price

    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.id"))
    pizza_id = db.Column(db.Integer, db.ForeignKey("pizzas.id"))

    # Defines relationship with Restaurant
    restaurant = db.relationship("Restaurant", back_populates="restaurantpizza")

    # Defines relationship with Pizza
    pizza = db.relationship("Pizza", back_populates="restaurantpizza")
