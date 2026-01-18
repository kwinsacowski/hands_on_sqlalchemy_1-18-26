from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///shop.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

    orders = relationship("Order", back_populates="user")

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    orders = relationship("Order", back_populates="product")

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    shipped = Column(Boolean, default=False)

    user = relationship("User", back_populates="orders")
    product = relationship("Product", back_populates="orders")

Base.metadata.create_all(engine)

#add try to look for existing users and products before adding new ones to avoid duplicates


for name, email in [('Alice', 'alice@example.com'), ('Bob', 'bob@example.com')]:
    if not session.query(User).filter_by(email=email).first():
        session.add(User(name=name, email=email))
    else:
        pass
session.commit()

for name, price in [('Laptop', 1000), ('Smartphone', 500), ('Headphones', 150)]:
    if not session.query(Product).filter_by(name=name).first():
        session.add(Product(name=name, price=price))
    else:
        pass
session.commit()

session.add(Order(user_id=1, product_id=1, quantity=1))
session.add(Order(user_id=1, product_id=2, quantity=2))
session.add(Order(user_id=2, product_id=2, quantity=1))
session.add(Order(user_id=2, product_id=3, quantity=2))


def get_user_info(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        return f"User: {user.name}, Email: {user.email}"
    return "User not found."

for user in session.query(User).all():
    print(get_user_info(user.id))

def get_product_info(product_id):
    product = session.query(Product).filter_by(id=product_id).first()
    if product:
        return f"Product: {product.name}, Price: {product.price}"
    return "Product not found."

for product in session.query(Product).all():
    print(get_product_info(product.id))

def get_order_info(order_id):
    order = session.query(Order).filter_by(id=order_id).first()
    if order:
        return f"Order ID: {order.id}, User: {order.user.name}, Product: {order.product.name}, Quantity: {order.quantity}"
    return "Order not found."

for order in session.query(Order).all():
    print(get_order_info(order.id)) 

#update a products price
def update_product_price(product_id, new_price):
    product = session.query(Product).filter_by(id=product_id).first()
    if product:
        product.price = new_price
        session.commit()
        return f"Updated {product.name} price to {new_price}"
    return "Product not found."

update_product_price(1, 900)
print(get_product_info(1))

def delete_user_by_id(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()
        return f"Deleted user {user.name}"
    return "User not found."

delete_user_by_id(2)