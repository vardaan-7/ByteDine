from fastapi import FastAPI
from app.user import User
from app.restaurant import Restaurant
from app.menu import MenuItem
from app.deliveryboy import DeliveryBoy
from app.order import Order
import pandas as pd
import os


app = FastAPI()

users = []
restaurants = []
deliveryboys = []
orders = []

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
            item = MenuItem(item_name,price)
            r.add_menu_item(item)
            return {"message": f"{item_name} added to menu"}
    return {"error": "Restaurant not found"}

@app.post("/signup/deliveryboy")
def signup_deliveryboy(name: str):
    deliveryboy = DeliveryBoy(name)
    deliveryboys.append(deliveryboy)
    return {"message": "Delivery partner signed up", "id": deliveryboy.delivery_boy_id}

@app.get("/restaurant/{restaurant_id}/menu")
def view_menu(restaurant_id: int):
    for r in restaurants:
        if r.restaurant_id == restaurant_id:
            return {
                "restaurant": r.name,
                "menu": [
                    {"item": item.name, "price": item.price}
                    for item in r.menu.values()  # Use .values() here
                ]
            }
    return {"error": "Restaurant not found"}

@app.post("/order")
def place_order(user_id: int, restaurant_id: int, item_name: str):
    # Find user object
    user = next((u for u in users if u.user_id == user_id), None)
    if not user:
        return {"error": "User not found"}

    # Find restaurant object
    restaurant = next((r for r in restaurants if r.restaurant_id == restaurant_id), None)
    if not restaurant:
        return {"error": "Restaurant not found"}

    # Find item object from restaurant menu
    item = restaurant.menu.get(item_name)
    if not item:
        return {"error": "Item not found in restaurant menu"}

    # Create order
    order = Order(user, restaurant, item)
    orders.append(order)
    restaurant.receive_order(order)

    return {
        "message": "Order placed successfully!",
        "order_id": order.order_id,
        "user": user.name,
        "restaurant": restaurant.name,
        "item": item.name,
        "price": item.price
    }