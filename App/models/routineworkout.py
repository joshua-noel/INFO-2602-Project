from App.database import db

class RoutineWorkout(db.Model): # Stores workouts that have been added to a user's routine(s)
    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'))
    routine_id = db.Column(db.Integer, db.ForeignKey('routine.id'))
    workout = db.relationship('Workout')

    def __init__(self, workout_id, routine_id, name, duration):
        self.workout_id = workout_id
        self.routine_id = routine_id
        self.name = name
        self.duration = duration
    
    def get_json(self):
        return {
            "id": self.id,
            "workout_id": self.workout_id,
            "routine_id": self.routine_id
        }