from App.database import db

# Looking at the requirements it would be simplest if workouts are pre-defined and users can just choose from them to add to routines
# Nothing suggests that users need to be able to make/add their own workout, only browse them and add to routines

class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    set_count = db.Column(db.Integer)
    rep_count = db.Column(db.Integer)

    def __init__(self, name, set_count, rep_count):
        self.name = name
        self.set_count = set_count
        self.rep_count = rep_count

    def get_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "set_count": self.set_count,
            "rep_count": self.rep_count
        }