from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class DeliveryBoy(Base):
    __tablename__ = 'delivery_boys'

    delivery_boy_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    available = Column(Boolean, default=True)
