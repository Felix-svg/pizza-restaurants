from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)


## Models
class Restaurant(db.Model, SerializerMixin):
    __tablename__ = "restaurants"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)

    @validates("name")
    def validates_name(self, key, name):
        if len(name.strip()) == 0:
            raise ValueError("Restaurant name cannot be empty.")
        if len(name.strip()) > 50:
            raise ValueError("Restaurant name must be less that 50 words.")
        return name

    def __repr__(self):
        return f"<Restaurant {self.id}, {self.name}>"


class Pizza(db.Model, SerializerMixin):
    __tablename__ = "pizzas"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    flavor = db.Column(db.String)

    def __repr__(self):
        return f"<Pizza {self.id}, {self.name}, {self.flavor}>"


class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = "restaurantpizza"
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)

    @validates("price")
    def validate_price(self, key, price):
        if price < 1 or price > 30:
            raise ValueError("Price must be between 1 and 30.")
        return price

    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.id"))
    pizza_id = db.Column(db.Integer, db.ForeignKey("pizzas.id"))
