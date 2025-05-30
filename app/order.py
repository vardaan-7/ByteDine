from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.restaurant_id'))
    item_id = Column(Integer, ForeignKey('menu_items.item_id'))
    quantity = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)

    group_id = Column(Integer, ForeignKey('order_groups.group_id'), nullable=True)

    user = relationship("User")
    restaurant = relationship("Restaurant")
    item = relationship("MenuItem")

    order_group = relationship("OrderGroup", back_populates="orders")
