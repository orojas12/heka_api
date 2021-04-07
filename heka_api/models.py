from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import post_load

db = SQLAlchemy()
ma = Marshmallow()

class VaccineContainer(db.Model):
    __tablename__ = 'vaccine_containers'

    id = db.Column(db.String(100), primary_key=True)
    order_id = db.Column(db.Integer)
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturers.id'))
    dist_center = db.Column(db.Integer, db.ForeignKey('distribution_centers.id'))

class VaccineSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = VaccineContainer
        include_fk = True

    @post_load
    def to_object(self, data, **kwargs):
        return VaccineContainer(**data)

class Manufacturer(db.Model):
    __tablename__ = 'manufacturers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    street = db.Column(db.String(50))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    province = db.Column(db.String(50))
    zip = db.Column(db.String(15))
    country = db.Column(db.String(50))

class ManufacturerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Manufacturer
        include_fk = True
        load_instance = True

    @post_load
    def to_object(self, data, **kwargs):
        return Manufacturer(**data)

class DistributionCenter(db.Model):
    __tablename__ = 'distribution_centers'

    id = db.Column(db.Integer, primary_key=True)

class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    company = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    street = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    zip = db.Column(db.String(15), nullable=False)
    dist_center = db.Column(db.Integer, db.ForeignKey('distribution_centers.id'), nullable=False)

class CustomerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Customer
        include_fk = True
    
    @post_load
    def to_object(self, data, **kwargs):
        return Customer(**data)

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    ship_address_same_as_customer = db.Column(db.Boolean)
    ship_street = db.Column(db.String(50))
    ship_city = db.Column(db.String(50))
    ship_state = db.Column(db.String(50))
    ship_zip = db.Column(db.String(15))
    date_placed = db.Column(db.DateTime)
    date_shipped = db.Column(db.DateTime)
    date_delivered = db.Column(db.DateTime)

class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        include_fk = True
    
    @post_load
    def to_object(self, data, **kwargs):
        return Order(**data)