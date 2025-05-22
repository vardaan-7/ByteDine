from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class DeliveryBoy(Base):
    __tablename__ = 'delivery_boys'
    
    delivery_boy_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    is_available = Column(Boolean, default=True)
    
    # You can add more fields like contact, rating, etc., if needed