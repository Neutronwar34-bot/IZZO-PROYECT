

# 🔥 PRIMERO tablas sin FK
from .category import Category
from .brand import Brand
from izzoApp.utils.db import db
# 🔥 DESPUÉS tablas con FK
from .product import Product
from .user import User
from .role import Role
from .authToken import AuthToken
from .location import Location
from .stock import Stock
from .stock_movement import StockMovement
from .supplier import Supplier
from .customer import Customer



