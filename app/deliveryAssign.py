from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class DeliveryAssignment(Base):
    __tablename__ = "delivery_assignments"

    id = Column(Integer, primary_key=True, index=True)
    order_group_id = Column(Integer, ForeignKey("order_groups.group_id"), unique=True)
    delivery_boy_id = Column(Integer, ForeignKey("delivery_boys.delivery_boy_id"))
    assigned_at = Column(DateTime, default=datetime.utcnow)

    order_group = relationship("OrderGroup")
    delivery_boy = relationship("DeliveryBoy")
