from sqlalchemy import Column, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from app.database import Base

class OrderGroup(Base):
    __tablename__ = "order_groups"

    group_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    delivery_boy_id = Column(Integer, ForeignKey("delivery_boys.delivery_boy_id"), nullable=True)
    delivery_boy = relationship("DeliveryBoy")

    orders = relationship("Order", back_populates="order_group")
