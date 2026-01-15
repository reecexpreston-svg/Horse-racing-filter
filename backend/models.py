from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Race(db.Model):
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
            'prize': self.prize
        }

class Runner(db.Model):
    __tablename__ = 'runners'
    id = db.Column(db.Integer, primary_key=True)
    race_id = db.Column(db.Integer, db.ForeignKey('races.id'), nullable=False, index=True)
    horse_name = db.Column(db.String(100), nullable=False, index=True)
    age = db.Column(db.Integer)
    weight = db.Column(db.String(20))
    draw = db.Column(db.Integer)
    jockey = db.Column(db.String(100), index=True)
    trainer = db.Column(db.String(100), index=True)
    official_rating = db.Column(db.Integer)
    form = db.Column(db.String(50))
    
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
            'form': self.form
        }
        if include_form:
            result['form_lines'] = [fl.to_dict() for fl in self.form_lines]
        return result

class FormLine(db.Model):
    __tablename__ = 'form_lines'
    id = db.Column(db.Integer, primary_key=True)
    runner_id = db.Column(db.Integer, db.ForeignKey('runners.id'), nullable=False, index=True)
    race_date = db.Column(db.Date, index=True)
    course = db.Column(db.String(100), index=True)
    distance = db.Column(db.String(50), index=True)
    going = db.Column(db.String(50), index=True)
    race_class = db.Column(db.String(50), index=True)
    finishing_position = db.Column(db.Integer, index=True)
    beaten_distance = db.Column(db.String(20))
    official_rating = db.Column(db.Integer)
    
    def to_dict(self):
        return {
            'id': self.id,
            'race_date': self.race_date.isoformat() if self.race_date else None,
            'course': self.course,
            'distance': self.distance,
            'going': self.going,
            'race_class': self.race_class,
            'finishing_position': self.finishing_position,
            'beaten_distance': self.beaten_distance,
            'official_rating': self.official_rating
        }
