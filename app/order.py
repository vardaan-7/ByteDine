from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.restaurant_id'))
    item_id = Column(Integer, ForeignKey('menu_items.item_id'))

    # Optional: relationships
    user = relationship("User")
    restaurant = relationship("Restaurant")
    item = relationship("MenuItem")