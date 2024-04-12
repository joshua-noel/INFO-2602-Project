from App.models import Workout
from App.database import db

def get_all_workouts():
    return Workout.query.all()

def get_workout_by_id(id):
    return Workout.query.filter_by(id=id).first()

def get_workout_by_name(name):
    return Workout.query.filter_by(name=name).first()

def get_all_workouts_json():
    workouts = get_all_workouts()

    if not workouts:
        return []

    return [workout.get_json() for workout in workouts]