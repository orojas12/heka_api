from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import post_load

db = SQLAlchemy()
ma = Marshmallow()

class VaccineContainer(db.Model):
    __tablename__ = 'vaccine_containers'

    id = db.Column(db.String(100), primary_key=True)
    order_id = db.Column(db.Integer)
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturers.id'), nullable=False)
    dist_center = db.Column(db.Integer, db.ForeignKey('distribution_centers.id'), nullable=False)

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

