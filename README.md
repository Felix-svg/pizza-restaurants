# pizza-restaurants

## Author
- Felix Omondi

## Introduction
This project involves creating a Pizza Restaurant domain, and building out the Flask API to add the functionality for the required HTTP Requests.

### Models
The following relationships are :
- A Restaurant has many Pizzas through RestaurantPizza
- A Pizza has many Restaurants through RestaurantPizza
- A RestaurantPizza belongs to a Restaurant and belongs to a Pizza

### Validations
Add validations to the RestaurantPizza model:
- Must have a price between 1 and 30

Add validations to Restaurant Model:
- Must have a name less than 50 words in length
- Must have a unique name

### Routes
- GET /restaurants
- GET /restaurants/:idLinks to an external site.
- DELETE /restaurants/:id
- GET /pizzas
- POST /restaurant_pizzas

## License
This project is licensed under the terms of the [MIT](./LICENSE) License.
