from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():
    # Delete all rows in tables
    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()

    # Add restaurants
    Dominion_Pizza = Restaurant(
        name="Dominion Pizza", address="Good Italian, Ngong Road, 5th Avenue"
    )
    Pizza_Hut = Restaurant(
        name="Pizza Hut", address="Westgate Mall, Mwanzi Road, Nrb 100"
    )

    # Add pizzas
    Cheese = Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Cheese")
    Pepperoni = Pizza(
        name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni"
    )

    # Add restaurantpizzas
    rp1 = RestaurantPizza(price=25, restaurant=Dominion_Pizza, pizza=Cheese)
    rp2 = RestaurantPizza(price=28, restaurant=Pizza_Hut, pizza=Pepperoni)

    # Append pizzas to restaurants
    Dominion_Pizza.restaurantpizza.append(rp1)
    Pizza_Hut.restaurantpizza.append(rp2)

    # Commit changes to the database
    db.session.add_all([Dominion_Pizza, Pizza_Hut, Cheese, Pepperoni, rp1, rp2])
    db.session.commit()
