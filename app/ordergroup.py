from sqlalchemy import Column, Integer, ForeignKey, DateTime, func, String
from sqlalchemy.orm import relationship
from app.database import Base
from app.order import Order  # adjust import path if needed

class OrderGroup(Base):
    __tablename__ = "order_groups"

    group_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    delivery_boy_id = Column(Integer, ForeignKey("delivery_boys.delivery_boy_id"), nullable=True)
    delivery_boy = relationship("DeliveryBoy")
    status = Column(String, default="pending")

    # Specify the correct FK path
    orders = relationship(
        "Order",
        back_populates="order_group",
        foreign_keys="[Order.group_id]"
    )
