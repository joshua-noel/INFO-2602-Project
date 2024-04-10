from App.database import db

class Workout(db.Model): # Stores preset exercises/workouts for user to choose from
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    duration = db.Column(db.Integer)
    set_count = db.Column(db.Integer)
    rep_count = db.Column(db.Integer)
    image = db.Column(db.String(256))
    # allows us to reference a Workout object and its fields from RoutineWorkout table. Ex. 'RoutineWorkout.workout.duration'
    in_routines = db.relationship('RoutineWorkout', backref='workout')

    def __init__(self, name, duration, set_count, rep_count, image):
        self.name = name
        self.duration = duration
        self.set_count = set_count
        self.rep_count = rep_count
        self.image = image

    def get_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "duration": self.duration,
            "set_count": self.set_count,
            "rep_count": self.rep_count,
            "image": self.image
        }