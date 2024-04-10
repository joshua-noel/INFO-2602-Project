from App.database import db

class Routine(db.Model): # Stores all created routines, which are groups of one or more exercises (workouts)
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    duration =  db.Column(db.Integer)
    workouts = db.relationship('RoutineWorkout', backref='routine')

    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def get_json(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "duraiton": self.duration
        }