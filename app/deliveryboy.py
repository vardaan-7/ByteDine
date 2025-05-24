from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy.orm import Session
from fastapi import HTTPException

class DeliveryBoy(Base):
    __tablename__ = 'delivery_boys'
    
    delivery_boy_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    is_available = Column(Boolean, default=True)

def assign_delivery_boy(db: Session):
    delivery_boy = db.query(DeliveryBoy).filter(DeliveryBoy.is_available == True).first()
    if not delivery_boy:
        raise HTTPException(status_code=503, detail="No delivery boys available at the moment.")
    
    delivery_boy.is_available = False
    db.commit()
    db.refresh(delivery_boy)
    return delivery_boy
