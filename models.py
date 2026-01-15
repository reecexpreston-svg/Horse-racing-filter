"""
Database Models for Horse Racing Data
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Race(db.Model):
    """Race meeting information"""
    __tablename__ = 'races'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, index=True)
    course = db.Column(db.String(100), nullable=False, index=True)
    race_time = db.Column(db.String(10))
    race_name = db.Column(db.String(200))
    distance = db.Column(db.String(50))
    race_class = db.Column(db.String(50))
    going = db.Column(db.String(50), index=True)
    prize = db.Column(db.String(50))
    age_restriction = db.Column(db.String(50))
    
    # Relationships
    runners = db.relationship('Runner', backref='race', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date.isoformat(),
            'course': self.course,
            'race_time': self.race_time,
            'race_name': self.race_name,
            'distance': self.distance,
            'race_class': self.race_class,
            'going': self.going,
            'prize': self.prize,
            'age_restriction': self.age_restriction
        }

class Runner(db.Model):
    """Individual runner in a race"""
    __tablename__ = 'runners'
    
    id = db.Column(db.Integer, primary_key=True)
    race_id = db.Column(db.Integer, db.ForeignKey('races.id'), nullable=False, index=True)
    
    # Horse details
    horse_name = db.Column(db.String(100), nullable=False, index=True)
    age = db.Column(db.Integer)
    weight = db.Column(db.String(20))
    draw = db.Column(db.Integer)
    
    # Jockey/Trainer
    jockey = db.Column(db.String(100), index=True)
    trainer = db.Column(db.String(100), index=True)
    
    # Ratings and odds
    official_rating = db.Column(db.Integer)
    rpr = db.Column(db.Integer)  # Racing Post Rating
    ts = db.Column(db.Integer)   # Top Speed
    odds = db.Column(db.String(20))
    
    # Form string
    form = db.Column(db.String(50))
    
    # Relationships
    form_lines = db.relationship('FormLine', backref='runner', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self, include_form=True):
        result = {
            'id': self.id,
            'horse_name': self.horse_name,
            'age': self.age,
            'weight': self.weight,
            'draw': self.draw,
            'jockey': self.jockey,
            'trainer': self.trainer,
            'official_rating': self.official_rating,
            'rpr': self.rpr,
            'ts': self.ts,
            'odds': self.odds,
            'form': self.form
        }
        
        if include_form:
            result['form_lines'] = [fl.to_dict() for fl in self.form_lines]
        
        return result

class FormLine(db.Model):
    """Individual past performance entry for a horse"""
    __tablename__ = 'form_lines'
    
    id = db.Column(db.Integer, primary_key=True)
    runner_id = db.Column(db.Integer, db.ForeignKey('runners.id'), nullable=False, index=True)
    
    # Race details
    race_date = db.Column(db.Date, index=True)
    course = db.Column(db.String(100), index=True)
    distance = db.Column(db.String(50), index=True)
    going = db.Column(db.String(50), index=True)
    race_class = db.Column(db.String(50), index=True)
    race_type = db.Column(db.String(50), index=True)  # Chase, Hurdle, NH Flat, Turf Flat, All Weather
    race_code = db.Column(db.String(50), index=True)  # Hch, Nvh, Md, etc.
    
    # Course characteristics (mapped from course name)
    surface = db.Column(db.String(100))
    configuration = db.Column(db.String(100))
    lh_rh = db.Column(db.String(50))  # Left Handed, Right Handed, Other
    
    # Performance
    finishing_position = db.Column(db.Integer, index=True)
    beaten_distance = db.Column(db.String(20))
    weight_carried = db.Column(db.String(20))
    
    # Ratings on the day
    official_rating = db.Column(db.Integer)
    rpr = db.Column(db.Integer)
    
    # Other details
    jockey = db.Column(db.String(100))
    odds = db.Column(db.String(20))
    comment = db.Column(db.Text)
    
    def to_dict(self):
        return {
            'id': self.id,
            'race_date': self.race_date.isoformat() if self.race_date else None,
            'course': self.course,
            'distance': self.distance,
            'going': self.going,
            'race_class': self.race_class,
            'race_type': self.race_type,
            'race_code': self.race_code,
            'surface': self.surface,
            'configuration': self.configuration,
            'lh_rh': self.lh_rh,
            'finishing_position': self.finishing_position,
            'beaten_distance': self.beaten_distance,
            'weight_carried': self.weight_carried,
            'official_rating': self.official_rating,
            'rpr': self.rpr,
            'jockey': self.jockey,
            'odds': self.odds,
            'comment': self.comment
        }
