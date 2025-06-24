from core.enums import OrderStatus
from core.base import Base
import uuid
from datetime import datetime
from sqlalchemy import UUID, DateTime, ForeignKey, Numeric, Integer, Enum

from sqlalchemy.orm import mapped_column, Mapped

class Order(Base):
    __tablename__ = "order"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    buyer_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("user.id"))
    status: Mapped[OrderStatus] = mapped_column(Enum(OrderStatus), default=OrderStatus.new)
    total_price: Mapped[float] = mapped_column(Numeric(10, 2))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow())

class OrderItem(Base):
    __tablename__ = "order_item"

    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("order.id"))
    product_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("product.id"))
    quantity: Mapped[int] = mapped_column(Integer)
    price: Mapped[float] = mapped_column(Numeric(10, 2))
    ordered_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow())