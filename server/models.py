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
    
    # Define relationship with RestaurantPizza
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='restaurant', lazy=True)

    def __repr__(self):
        return f"<Restaurant {self.id}, {self.name}>"

class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = "restaurantpizza"
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))

    # Define relationship with Restaurant
    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas')
    # Define relationship with Pizza
    pizza = db.relationship('Pizza', back_populates='restaurant_pizzas')

    @validates("price")
    def validate_price(self, key, price):
        if price < 1 or price > 30:
            raise ValueError("Price must be between 1 and 30.")
        return price

class Pizza(db.Model, SerializerMixin):
    __tablename__ = "pizzas"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    flavor = db.Column(db.String(50))

    # Define relationship with RestaurantPizza
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='pizza', lazy=True)

    def __repr__(self):
        return f"<Pizza {self.id}, {self.name}, {self.flavor}>"

