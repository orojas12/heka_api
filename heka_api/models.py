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

    def __repr__(self):
        return "<VaccineContainer id={}, order_id={}, manufacturer_id={}, dist_center={}>".format(
            self.id, self.order_id, self.manufacturer_id, self.dist_center
        )

class VaccineSchema(ma.SQLAlchemySchema):
    class Meta:
        model = VaccineContainer
    
    id = ma.auto_field()
    order_id = ma.auto_field()
    manufacturer_id = ma.auto_field()
    dist_center = ma.auto_field()

    @post_load
    def to_object(self, data, **kwargs):
        return VaccineContainer(**data)

class Manufacturer(db.Model):
    __tablename__ = 'manufacturers'

    id = db.Column(db.Integer, primary_key=True)

class DistributionCenter(db.Model):
    __tablename__ = 'distribution_centers'

    id = db.Column(db.Integer, primary_key=True)

class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)

class CustomerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Customer
        include_fk = True
        load_instance = True

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
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
        load_instance = True
    
    @post_load
    def to_object(self, data, **kwargs):
        return Order(**data)