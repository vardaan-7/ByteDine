from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)

    # One user can have many orders
    order_history = relationship("Order", back_populates="user")

    def __init__(self, name):
        self.name = name

    def place_order(self, restaurant, item_name):
        if item_name in restaurant.menu:
            item = restaurant.menu[item_name]
            order = order.Order(user=self, restaurant=restaurant, item=item)
            self.order_history.append(order)
            restaurant.receive_order(order)
            print(f"{self.name} placed an order for {item.name}")
            return order
        else:
            print(f"{item_name} not found in {restaurant.name}'s menu.")
            return None

    def view_order_history(self):
        print(f"\nOrder history for {self.name}:")
        for order in self.order_history:
            print(f"-> {order.item.name} from {order.restaurant.name}")
