from database import db


class Route(db.Model):
    __tablename__ = 'routes'

    route_id = db.Column(db.Integer, primary_key=True)
    crag_id = db.Column(db.Integer, db.ForeignKey(
        'crags.crag_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.user_id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    difficulty_level = db.Column(db.String(50), nullable=False)
    route_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    photo = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(
    ), onupdate=db.func.current_timestamp())

    # Define relationships with other entities
    user = db.relationship('User', backref=db.backref('routes'))
    crag = db.relationship('Crag', backref=db.backref('routes'))

    # Add any additional attributes or methods as needed
