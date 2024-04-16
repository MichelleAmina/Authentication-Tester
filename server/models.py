from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

"""
class User(db.Mode):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    confirm_password = db.Column(db.String(80), nullable=False)
    user_type = db.Column(db.String())


class Shop(db.model):
    user_id = 
    orders = 


class Customer(db.Model):
    user_id
    orders =

    
class Orders
    client_id 
    total_price 

    shop
    customer 


class Order_products(db.Model):
    product_id 
    order_id
    quantity 



"""


class Admin(db.Model):

    __tablename__ = 'admins'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    company_name = db.Column(db.String)
    phone = db.Column(db.Integer)
    password = db.Column(db.String(80), nullable=False)
    confirm_password = db.Column(db.String(80), nullable=False)
    

    def __repr__(self):
        return f'<Admin {self.email} of company {self.company_name}>'