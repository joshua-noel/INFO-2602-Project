from App.models import routine
from App.database import db

def get_all_routines():
    return Routine.query.all()

def get_routine_by_name(name):
    return Routine.query.filter_by(name=name).first()

def get_all_routines_json():
    routines = get_all_routines()

    if not routines:
        return []

    return [routine.get_json() for routine in routines]

def create_routine(name, duration):
    routine = Routine(name=name, duration=duration)
    db.session.add(workout)
    return db.session.commit()

def update_routine(name, duration):
    routine = get_routine_by_name(name)

    if routine:
        routine.duration = duration
        db.session.add(workout)
        return db.session.commit()

    return None
