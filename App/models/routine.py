from App.database import db

class Routine(db.Model): # Stores all created routines, which are groups of one or more exercises (workouts)
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    duration =  db.Column(db.Integer)
    # allows us to reference a Routine object and its fields from RoutineWorkouts table. Ex. 'RoutineWorkout.routine.user_id'
    workouts_in_routine = db.relationship('RoutineWorkout', backref='routine')

    def __init__(self, user_id, name, duration):
        self.user_id = user_id
        self.name = name
        self.duration = duration

    def get_json(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "duraton": self.duration
        }