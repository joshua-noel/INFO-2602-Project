from App.models import Routine
from App.database import db

def get_all_routines():
    return Routine.query.all()

def get_routine_by_name(name):
    return Routine.query.filter_by(name=name).first()

def get_routine_by_id(id):
    return Routine.query.filter_by(id=id).first()

def get_all_routines_json():
    routines = get_all_routines()

    if not routines:
        return []

    return [routine.get_json() for routine in routines]

def update_routine(id, name, duration):
    routine = get_routine_by_id(id=id)

    if routine:
        routine.duration = duration
        routine.name = name
        db.session.add(routine)
        return db.session.commit()

    return None

def rename_routine(id, name):
    routine = get_routine_by_id(id=id)

    if routine:
        routine.name = name
        db.session.add(routine)
        return db.session.commit()

    return None


def add_workout(self, workout_id, name, duration):
    try:
        workout = RoutineWorkout(workout_id, name, duration)
        db.session.add(workout)
        db.session.commit()
        return workout

    except Exception as e:
        print(e)
        db.session.rollback()
        return None

    return None

