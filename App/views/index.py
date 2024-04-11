from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from flask_jwt_extended import jwt_required, current_user as jwt_current_user

from App.models import db
from App.controllers import (
    create_user,
    jwt_required,
    check_routine,
    create_routine,
    create_default_routine
)

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')

@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})

# Page Routes

@index_views.route("/app", methods=['GET'])
@index_views.route("/app/<int:routine_id>", methods=['GET'])
@jwt_required()
def home_page(routine_id=1):
    default_routine = Routine.query.filter_by(name = 'My Starter Routine').first()
    if default_routine:
            allroutines = Routine.query.all()
            allworkouts = Workout.query.all()
            routine = Routine.query.filter_by(id=routine_id).first()
            return render_template("index.html", allroutines = allroutines, allworkouts = allworkouts, routine = routine, current_user = current_user)
    else:
        create_default_routine(current_user)
        allroutines = Routine.query.all()
        allworkouts = Workout.query.all()
        routine = Routine.query.filter_by(id=routine_id).first()
        return render_template("index.html", allroutines = allroutines, allworkouts = allworkouts, routine = routine, current_user = current_user)

# Action Routes
@index_views.route("/pokemon/<int:routine_id>", methods=['POST'])
@jwt_required()
def create_routine_action(routine_id):
    data = request.form
    valid = current_user.check_routine(data['name'])
    if valid == True:
        current_user.create_routine(data['name'])
        flash('Routine created!')
        return redirect(url_for('home_page'))
    else:
        flash('A Routine of this name already exists!')
        return redirect(url_for('home_page'))
