from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    #routines = db.relationship('Routine', backref='user') ... this doesn't work, not sure if it's needed

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username
        }

    def create_routine(self, name, duration):
        exercise = Workout.query.get(workout_id)
        if exercise:
            try:
                workout = Routine(self.id, workout_id, name, duration)
                db.session.add(workout)
                db.session.commit()
                return workout
            except Exception as e:
                print(e)
                db.session.rollback()
                return None
        return None

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

