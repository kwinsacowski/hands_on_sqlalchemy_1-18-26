SQLAlchemy Shop Database Example
📌 Overview

This project demonstrates how to create and manage a relational database using Python and SQLAlchemy ORM.
It includes table definitions, relationships, and basic CRUD operations using an SQLite database.

The database models a simple shop system with:

Users
Products
Orders (including shipped status)

--------------------------------

🛠️ Requirements

Python 3.9+
SQLAlchemy

-------------------------------
📦 Installation

Clone or download this repository.
(Optional but recommended) Create a virtual environment:
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:
    pip install SQLAlchemy

--------------------------------
Running the Application

Ensure you are in the project directory.
Run the Python script:
    python shop.py

This will:
Create the shop.db SQLite database (if it does not exist)
Create all tables
Insert sample users, products, and orders
Run example queries and print results to the console

------------------------------

🗄️ Database Schema

User
    id (Primary Key)
    name
    email (Unique)

Product
    id (Primary Key)
    name
    price

Order
    id (Primary Key)
    user_id (Foreign Key → users.id)
    product_id (Foreign Key → products.id)
    quantity
    shipped (Boolean)

------------------------------

🔗 Relationships

A User can have many Orders
A Product can appear in many Orders
Deleting a user automatically deletes their orders (cascade delete)

-----------------------------

🧪 Example Operations Performed

Insert users and products (with duplicate checks)
Create orders using ORM relationships (no hard-coded IDs)
Retrieve and display:
    All users
    All products
    All orders with user and product details
Update a product’s price
Delete a user by ID

----------------------

✅ Notes

The project uses SQLAlchemy ORM best practices
Foreign keys are managed automatically through relationships
IDs are never hard-coded when creating related records

------------------------

📚 Technologies Used

Python
SQLAlchemy
SQLite