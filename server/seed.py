from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():
    # Delete all rows in tables
    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()

    # Add restaurants
    Bella_Italia_Trattoria = Restaurant(name="Bella Italia Trattoria")
    The_Rusty_Spoon = Restaurant(name="The Rusty Spoon")
    Sakura_Sushi_Bar = Restaurant(name="Sakura Sushi Bar")

    # Add pizzas
    margherita = Pizza(name="margherita", flavor="mozzarella cheese")
    pepperoni = Pizza(name="pepperoni", flavor="pepperoni slices")
    hawaiian = Pizza(name="hawaiian", flavor="pineapple")

    # Add restaurantpizzas
    rp1 = RestaurantPizza(price=25, restaurant=Bella_Italia_Trattoria, pizza=margherita)
    rp2 = RestaurantPizza(price=28, restaurant=The_Rusty_Spoon, pizza=pepperoni)
    rp3 = RestaurantPizza(price=26, restaurant=Sakura_Sushi_Bar, pizza=hawaiian)

    # Append pizzas to restaurants
    Bella_Italia_Trattoria.restaurant_pizzas.append(rp1)
    The_Rusty_Spoon.restaurant_pizzas.append(rp2)
    Sakura_Sushi_Bar.restaurant_pizzas.append(rp3)

    # Commit changes to the database
    db.session.add_all(
        [
            Bella_Italia_Trattoria,
            The_Rusty_Spoon,
            Sakura_Sushi_Bar,
            margherita,
            pepperoni,
            hawaiian,
            rp1,
            rp2,
            rp3,
        ]
    )
    db.session.commit()
