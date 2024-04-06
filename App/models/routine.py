from App.database import db

class Routine(db.Model): #A group of one or more exercises
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'))
    name = db.Column(db.String(120), nullable=False)
    duration =  db.Column(db.Integer)
    workout = db.relationship('Workout', backref='routine')

    def __init__(self, workout_id, name, duration):
        self.workout_id = workout_id
        self.name = name
        self.duration = duration