from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from app.ordergroup import OrderGroup
from app.database import SessionLocal, engine, Base
from app.user import User
from app.restaurant import Restaurant
from app.menu import MenuItem
from app.order import Order
from app.deliveryboy import DeliveryBoy

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic models for request validation
class OrderItem(BaseModel):
    restaurant_id: int
    item_name: str
    quantity: int = 1

class MultipleOrderRequest(BaseModel):
    user_id: int
    items: List[OrderItem]

@app.get("/")
def home():
    return {"message": "Welcome to ByteDine API"}

@app.post("/signup/user")
def signup_user(name: str, db: Session = Depends(get_db)):
    user = User(name=name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": f"User {name} signed up successfully", "user_id": user.user_id}

@app.post("/signup/restaurant")
def signup_restaurant(name: str, location: str, db: Session = Depends(get_db)):
    restaurant = Restaurant(name=name, location=location)
    db.add(restaurant)
    db.commit()
    db.refresh(restaurant)
    return {"message": "Restaurant signed up", "id": restaurant.restaurant_id}

@app.post("/restaurant/{restaurant_id}/add_menu_item")
def add_menu_item(restaurant_id: int, item_name: str, price: int, db: Session = Depends(get_db)):
    restaurant = db.query(Restaurant).filter(Restaurant.restaurant_id == restaurant_id).first()
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")

    # Create menu item and associate with restaurant
    menu_item = MenuItem(name=item_name, price=price, restaurant_id=restaurant_id)
    db.add(menu_item)
    db.commit()
    db.refresh(menu_item)
    return {"message": f"{item_name} added to menu"}

@app.post("/signup/deliveryboy")
def signup_deliveryboy(name: str, db: Session = Depends(get_db)):
    deliveryboy = DeliveryBoy(name=name)
    db.add(deliveryboy)
    db.commit()
    db.refresh(deliveryboy)
    return {"message": "Delivery partner signed up", "id": deliveryboy.delivery_boy_id}

@app.get("/restaurant/{restaurant_id}/menu")
def view_menu(restaurant_id: int, db: Session = Depends(get_db)):
    restaurant = db.query(Restaurant).filter(Restaurant.restaurant_id == restaurant_id).first()
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")

    menu = db.query(MenuItem).filter(MenuItem.restaurant_id == restaurant_id).all()

    return {
        "restaurant": restaurant.name,
        "menu": [{"item": item.name, "price": item.price} for item in menu]
    }

@app.get("/restaurants")
def list_restaurants(db: Session = Depends(get_db)):
    restaurants = db.query(Restaurant).all()
    return {
        "restaurants": [
            {"id": r.restaurant_id, "name": r.name, "location": r.location} 
            for r in restaurants
        ]
    }

@app.get("/order-options")
def get_order_options(db: Session = Depends(get_db)):
    # Get all restaurants
    restaurants = db.query(Restaurant).all()
    
    result = []
    for restaurant in restaurants:
        # Get menu items for each restaurant
        menu_items = db.query(MenuItem).filter(MenuItem.restaurant_id == restaurant.restaurant_id).all()
        
        result.append({
            "restaurant_id": restaurant.restaurant_id,
            "restaurant_name": restaurant.name,
            "location": restaurant.location,
            "menu": [
                {"item_name": item.name, "price": item.price}
                for item in menu_items
            ]
        })
    
    return {"order_options": result}

@app.post("/order")
def place_order(user_id: int, restaurant_id: int, item_name: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    restaurant = db.query(Restaurant).filter(Restaurant.restaurant_id == restaurant_id).first()
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")

    item = db.query(MenuItem).filter(
        MenuItem.restaurant_id == restaurant_id,
        MenuItem.name == item_name
    ).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found in restaurant menu")

    order = Order(user_id=user.user_id, restaurant_id=restaurant.restaurant_id, item_id=item.item_id)
    db.add(order)
    db.commit()
    db.refresh(order)

    return {
        "message": "Order placed successfully!",
        "order_id": order.order_id,
        "user": user.name,
        "restaurant": restaurant.name,
        "item": item.name,
        "price": item.price
    }

@app.post("/place-multiple-orders")
def place_multiple_orders(order_request: MultipleOrderRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == order_request.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Create new OrderGroup
    order_group = OrderGroup(user_id=user.user_id)
    db.add(order_group)
    db.commit()
    db.refresh(order_group)

    placed_orders = []
    total_price = 0

    for item_request in order_request.items:
        restaurant = db.query(Restaurant).filter(
            Restaurant.restaurant_id == item_request.restaurant_id
        ).first()
        if not restaurant:
            raise HTTPException(status_code=404, detail="Restaurant not found")

        menu_item = db.query(MenuItem).filter(
            MenuItem.restaurant_id == item_request.restaurant_id,
            MenuItem.name == item_request.item_name
        ).first()
        if not menu_item:
            raise HTTPException(status_code=404, detail="Item not found in menu")

        for _ in range(item_request.quantity):
            order = Order(
                user_id=user.user_id,
                restaurant_id=restaurant.restaurant_id,
                item_id=menu_item.item_id,
                group_id=order_group.group_id  # Assign group ID here
            )
            db.add(order)
            db.commit()
            db.refresh(order)

            placed_orders.append({
                "order_id": order.order_id,
                "restaurant": restaurant.name,
                "item": menu_item.name,
                "price": menu_item.price
            })

            total_price += menu_item.price

    return {
        "message": f"Successfully placed {len(placed_orders)} orders",
        "group_id": order_group.group_id,
        "user": user.name,
        "orders": placed_orders,
        "total_price": total_price
    }
