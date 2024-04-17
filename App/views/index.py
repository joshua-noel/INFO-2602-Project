from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, flash, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
import csv

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
    get_all_routineworkouts,
    remove_workout_from_routine,
    get_all_workouts_in_routine
)

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route("/", methods=['GET'])
@index_views.route("/<id>", methods=['GET'])
@jwt_required()
def index_page(id=1):
    default_routine = get_routine_by_id(id=1)
    totalDuration = 0

    if default_routine:
        allroutines = get_all_routines()
        allworkouts = get_all_workouts()
        routineworkouts = get_all_routineworkouts()
        selected_routine = get_routine_by_id(id=id)
        user_routine_workouts = get_all_workouts_in_routine(routine_id=id)

        for workout in user_routine_workouts:
            totalDuration += workout.workout.duration

        return render_template("index.html", allroutines = allroutines, allworkouts = allworkouts, routineworkouts = routineworkouts, selected_routine = selected_routine, totalDuration=(totalDuration/60), current_user = jwt_current_user)
    else:
        default_routine = create_default_routine(jwt_current_user)
        allroutines = get_all_routines()
        allworkouts = get_all_workouts()
        routineworkouts = get_all_routineworkouts()
        selected_routine = get_routine_by_id(id=default_routine.id)
        user_routine_workouts = get_all_workouts_in_routine(routine_id=default_routine.id)

        for workout in user_routine_workouts:
            totalDuration += workout.workout.duration

        return render_template("index.html", allroutines = allroutines, allworkouts = allworkouts, routineworkouts = routineworkouts, selected_routine = selected_routine, totalDuration=(totalDuration/60), current_user = jwt_current_user)

@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')

    with open('workouts.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            workout = Workout(name=row['Name'],
                                set_count=row['Sets'],
                                rep_count=row['Reps'], 
                                duration =row['Duration'], 
                                image =row['Image'])
            db.session.add(workout)
            db.session.commit()

    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})

# Action Routes

@index_views.route("/createRoutine", methods=['POST'])
@jwt_required()
def create_routine_action():
    data = request.form
    exists = check_routine(jwt_current_user, name=data['routine_name'])

    if not exists:
        routine = create_routine(jwt_current_user, name=data['routine_name'])
        flash('Routine created!')
        return redirect(url_for('index_views.index_page', id=routine.id))
    else:
        flash('A Routine of this name already exists!')
        return redirect(url_for('index_views.index_page', id=exists.id))

@index_views.route("/renameRoutine/<id>", methods=['POST'])
@jwt_required()
def rename_routine_action(id=id):
    data = request.form
    exists = check_routine(jwt_current_user, name=data['routine_rename'])

    if not exists:
        rename_routine(id=id, name=data['routine_rename'])
        flash('Routine renamed!')
        return redirect(url_for('index_views.index_page', id=id))
    else:
        flash('A Routine of this name already exists!')
        return redirect(url_for('index_views.index_page', id=id))

@index_views.route("/addWorkout/<selected_routine_id>/<workout_id>", methods=['GET'])
@jwt_required()
def add_workout_to_routine_action(selected_routine_id, workout_id):
    workout_in_routine = check_workout(jwt_current_user, routine_id=selected_routine_id, workout_id=workout_id)

    if workout_in_routine:
        add_workout_to_routine(jwt_current_user, routine_id=selected_routine_id, workout_id=workout_id)
        flash('Workout added!')
        return redirect(url_for('index_views.index_page', id=selected_routine_id))
    else: 
        flash('Workout already exists in this routine!')
        return redirect(url_for('index_views.index_page', id=selected_routine_id))

@index_views.route("/deleteWorkout/<selected_routine_id>/<workout_id>", methods=['GET'])
@jwt_required()
def delete_workout_from_routine_action(selected_routine_id, workout_id):
    workout_in_routine = check_workout(jwt_current_user, routine_id=selected_routine_id, workout_id=workout_id)

    if not workout_in_routine:
        remove_workout_from_routine(jwt_current_user, routine_id=selected_routine_id, workout_id=workout_id)
        flash('Workout removed!')
        return redirect(url_for(f'index_views.index_page', id=selected_routine_id))
    else: 
        flash('Workout does not exist in this routine!')
        return redirect(url_for('index_views.index_page', id=selected_routine_id))
