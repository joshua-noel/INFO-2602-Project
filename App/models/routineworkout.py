from App.database import db

class RoutineWorkout(db.Model): # Stores the workouts that have been added to a users' routine(s)
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'))
    routine_id = db.Column(db.Integer, db.ForeignKey('routine.id'))

    def __init__(self, workout_id, routine_id, name, duration):
        self.user_id = user_id
        self.workout_id = workout_id
        self.routine_id = routine_id
    
    def get_json(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "workout_id": self.workout_id,
            "routine_id": self.routine_id
        }