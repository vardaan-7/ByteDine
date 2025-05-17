from fastapi import FastAPI
from app.user import User
from app.restaurant import Restaurant
from app.menu import MenuItem
from app.deliveryboy import DeliveryBoy
from app.order import Order


app = FastAPI()

users = []
restaurants = []
deliveryboys = []

@app.get("/")
def home():
    return {"message": "Welcome to ByteDine API"}

@app.post("/signup/user")
def signup_user(name: str):
    user = User(name)
    users.append(user)
    return {"message": f"User {name} signed up successfully", "user_id": user.user_id}

@app.post("/signup/restaurant")
def signup_restaurant(name: str, location: str):
    restaurant = Restaurant(name, location)
    restaurants.append(restaurant)
    return {"message": "Restaurant signed up", "id": restaurant.restaurant_id}

@app.post("/restaurant/{restaurant_id}/add_menu_item")
def add_menu_item(restaurant_id: int, item_name: str, price: int):
    for r in restaurants:
        if r.restaurant_id == restaurant_id:
            r.add_menu_item(item_name, price)
            return {"message": f"{item_name} added to menu"}
    return {"error": "Restaurant not found"}

@app.get("/restaurant/{restaurant_id}/menu")
def view_menu(restaurant_id: int):
    for r in restaurants:
        if r.restaurant_id == restaurant_id:
            return {
                "restaurant": r.name,
                "menu": [
                    {"item": item, "price": price}
                    for item, price in r.menu.items()
                ]
            }
    return {"error": "Restaurant not found"}
