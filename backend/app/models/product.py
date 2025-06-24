from datetime import datetime
import uuid
from core.base import Base
from sqlalchemy import UUID, Boolean, DateTime, Enum, ForeignKey, Numeric, String, Integer, Text

from core.enums import AttributeType, ProductStatus
from sqlalchemy.orm import mapped_column, Mapped

class ProductCategory(Base):
    __tablename__ = "product_category"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    parent_id: Mapped[int | None] = mapped_column(ForeignKey("product_category.id"), nullable=False)

class Product(Base):
    __tablename__ = "product"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    seller_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    category_id: Mapped[int] = mapped_column(ForeignKey("product_category.id"))
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text)
    price: Mapped[float] = mapped_column(Numeric(10, 2))
    quantity: Mapped[int] = mapped_column(Integer, default=0)
    status: Mapped[ProductStatus] = mapped_column(Enum(ProductStatus), default=ProductStatus.draft)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

class ProductAttribute(Base):
    __tablename__ = "product_attribute"

    id: Mapped[int] = mapped_column(primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("product_category.id", ondelete="CASCADE"))
    name: Mapped[str] = mapped_column(String(100))
    type: Mapped[AttributeType] = mapped_column(Enum(AttributeType))

class ProductAttributeValue(Base):
    __tablename__ = "product_attribute_value"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("product.id"))
    attribute_id: Mapped[int] = mapped_column(ForeignKey("product_attribute.id"))
    value: Mapped[str] = mapped_column(Text)

class ProductImage(Base):
    __tablename__ = "product_image"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("product.id"))
    url: Mapped[str] = mapped_column(Text)
    is_main: Mapped[bool] = mapped_column(Boolean, default=False)
