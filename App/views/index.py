from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, flash, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user

from App.models import *
from App.controllers import (
    create_user,
    jwt_required,
    check_routine,
    create_routine,
    create_default_routine,
    get_all_workouts,
    get_all_routines,
    get_routine_by_id,
    rename_routine,
    check_workout,
    add_workout_to_routine,
    get_all_routineworkouts
)

index_views = Blueprint('index_views', __name__, template_folder='../templates')

# @index_views.route('/', methods=['GET'])
# def index_page():
#     return render_template('index.html')

# @index_views.route('/init', methods=['GET'])
# def init():
#     db.drop_all()
#     db.create_all()
#     create_user('bob', 'bobpass')
#     return jsonify(message='db initialized!')

# @index_views.route('/health', methods=['GET'])
# def health_check():
#     return jsonify({'status':'healthy'})

# Page Routes

@index_views.route("/", methods=['GET'])
@index_views.route("/<id>", methods=['GET']) #"/<int:routine_id>"
@jwt_required()
def index_page(id=1):
    default_routine = get_routine_by_id(id=1)

    if default_routine:
        allroutines = get_all_routines()
        allworkouts = get_all_workouts()
        routineworkouts = get_all_routineworkouts()
        selected_routine = get_routine_by_id(id=id)
        return render_template("index.html", allroutines = allroutines, allworkouts = allworkouts, routineworkouts = routineworkouts, selected_routine = selected_routine, current_user = jwt_current_user)
    else:
        default_routine = create_default_routine(jwt_current_user)
        allroutines = get_all_routines()
        allworkouts = get_all_workouts()
        routineworkouts = get_all_routineworkouts()
        selected_routine = get_routine_by_id(id=default_routine.id)
        return render_template("index.html", allroutines = allroutines, allworkouts = allworkouts, routineworkouts = routineworkouts, selected_routine = selected_routine, current_user = jwt_current_user)

@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})

# Action Routes

@index_views.route("/createRoutine", methods=['POST'])
@jwt_required()
def create_routine_action():
    data = request.form
    valid = check_routine(jwt_current_user, name=data['routine_name'])

    if valid == True:
        create_routine(jwt_current_user, name=data['routine_name'])
        flash('Routine created!')
        return redirect(url_for('index_views.index_page'))
    else:
        flash('A Routine of this name already exists!')
        return redirect(url_for('index_views.index_page'))

@index_views.route("/renameRoutine/<id>", methods=['POST'])
@jwt_required()
def rename_routine_action(id=id):
    data = request.form
    valid = check_routine(jwt_current_user, name=data['routine_rename'])

    if valid == True:
        rename_routine(id=id, name=data['routine_rename'])
        flash('Routine renamed!')
        return redirect(url_for('index_views.index_page'))
    else:
        flash('A Routine of this name already exists!')
        return redirect(url_for('index_views.index_page'))

# unsolved error: TypeError: add_workout_to_routine_action() got an unexpected keyword argument 'selected_routine_id'

# @index_views.route("/addWorkout/<selected_routine_id>/<workout_id>", methods=['GET'])
# @jwt_required()
# def add_workout_to_routine_action():#(selected_routine_id= selected_routine_id, workout_id= workout_id):
#     valid = check_workout(jwt_current_user, selected_routine_id, workout_id)
#     if valid == True:
#         add_workout_to_routine(routine_id = selected_routine_id, workout_id = workout_id)
#         flash('Workout added!')
#         return redirect(url_for('index_views.index_page'))
#     else: 
#         flash('Workout already exists in this routine!')
#         return redirect(url_for('index_views.index_page'))
