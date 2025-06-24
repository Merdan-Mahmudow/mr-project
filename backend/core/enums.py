import enum


class UserRole(str, enum.Enum):
    buyer: str = "buyer"
    seller: str = "seller"
    admin: str = "admin"

class ProductStatus(str, enum.Enum):
    active: str = "active"
    inactive: str = "inactive"
    draft: str = "draft"
    banned: str = "banned"

class AttributeType(str, enum.Enum):
    text: str = "text"
    number: str = "number"
    select: str = "select"
    boolean: str = "boolean"

class OrderStatus(str, enum.Enum):
    new: str = "new"
    paid: str = "paid"
    shipped: str = "shipped"
    done: str = "done"
    cencelled: str = "cencelled"