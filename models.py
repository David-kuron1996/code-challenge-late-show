from app import db
from datetime import datetime

class Episode(db.Model):
    __tablename__ = 'episodes'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    appearances = db.relationship('Appearance', backref='episode', cascade='all, delete-orphan')
    
    def to_dict(self, include_appearances=False):
        data = {
            'id': self.id,
            'date': self.date,
            'number': self.number
        }
        if include_appearances:
            data['appearances'] = [appearance.to_dict() for appearance in self.appearances]
        return data
class Guest(db.Model):
    __tablename__ = 'guests'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    occupation = db.Column(db.String(100), nullable=False)
    appearances = db.relationship('Appearance', backref='guest', cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'occupation': self.occupation
        }

class Appearance(db.Model):
    __tablename__ = 'appearances'
    
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)
    