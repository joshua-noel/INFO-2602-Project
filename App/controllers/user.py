from App.models import User, Routine
from App.database import db

def create_user(username, password):
    newuser = User(username=username, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None

# Create routine functions 
# To be used by action routes in index.py view

def create_default_routine(self):
    routine = Routine(self.id,'My Starter Routine', None)
    db.session.add(routine)
    db.session.commit()
    return routine

def check_routine(self, name):
    valid = True
    check = Routine.query.filter_by(name = name, user_id = self.id).first()
    if check:
            valid = False
            return valid
    else:
        return valid

def create_routine(self, name):
    routine = Routine(user_id = self.id, name = name, duration = None)
    db.session.add(routine)
    db.session.commit()
    return routine

    