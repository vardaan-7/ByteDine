from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class MenuItem(Base):
    __tablename__ = 'menu_items'
    
    item_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    
    restaurant_id = Column(Integer, ForeignKey('restaurants.restaurant_id'))
    restaurant = relationship("Restaurant", back_populates="menu_items")
    
    # Define relationship with Order
    orders = relationship("Order")