from App.models import RoutineWorkout
from App.database import db

def get_all_routineworkouts():
    return RoutineWorkout.query.all()

def get_all_routines_json():
    routine_workouts = get_all_routine_workouts()

    if not routine_workouts:
        return []

    return [routine_workout.get_json() for routine_workout in routine_workouts]