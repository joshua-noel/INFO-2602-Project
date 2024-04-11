from App.models import workout
from App.database import db

def get_all_workouts():
    return Workout.query.all()

def get_workout_by_name(name):
    return Workout.query.filter_by(name=name).first()

def get_all_workouts_json():
    workouts = get_all_workouts()

    if not workouts:
        return []

    return [workout.get_json() for workout in workouts]

# def update_workout(name, set_count, rep_count):
#     workout = get_workout_by_name(name)

#     if workout:
#         workout.name = name
#         workout.set_count = set_count
#         workout.rep_count = rep_count
#         db.session.add(workout)
#         return db.session.commit()

#     return None