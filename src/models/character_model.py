from db.db import db


class Character(db.Model):
    __tablename__ = 'characters'

    character_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    health = db.Column(db.Integer, nullable=False)
    armor_class = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    x_coordinate = db.Column(db.Float, default=0.0)
    y_coordinate = db.Column(db.Float, default=0.0)

    def __repr__(self):
        return f'<Character {self.name}>'
