from flask import Blueprint, flash, render_template, redirect, url_for, request, jsonify
import flask_login

from models import Course, Session, Student, Enrolled
from forms import ChoiceForm
from extension import db


bp2 = Blueprint('view', __name__)

@bp2.route('/user', methods=['GET', 'POST'])
def get_data():
    form = ChoiceForm()
    user = flask_login.current_user
    get_student = user.student_enrolled

    x_list = []
    for subject in get_student:
        subjects = subject.course
        x_list.append(subjects)

    course_list = Course.query.all()
    get_course = []
    for course in course_list:
        subjects = course
        get_course.append(subjects)


    form.option.query = []
    for subject in get_course:
        if subject not in x_list:
            form.option.query.append(subject)


    if form.validate_on_submit():
        register_subject = Enrolled(student=user, course=form.option.data, session=form.timeslot.data)

        db.session.add(register_subject)
        db.session.commit()
        flash(f'The subject {form.option.data} has been registered!')
        return redirect(url_for('view.get_data'))

    return render_template('user.html', form=form, registered=get_student, user=user)


@bp2.route('/<int:cid>/<int:sid>/delete', methods=['GET', 'POST'])
def delete(cid, sid):
    user = flask_login.current_user
    schedule = Enrolled.query.filter_by(student_id=user.id).filter_by(course_id=cid).filter_by(session_id=sid)

    if request.method == "POST":
        schedule.delete()
        db.session.commit()

        flash(f'Subject select has been deleted.')
        return redirect(url_for('view.get_data'))
    
    return render_template('delete.html')


@bp2.route('/session/<id>')
def session(id):
    schedule = db.session.query(Session.id, Session.datetime).join(Course).filter(Course.id == id).all()

    sessionArray = []

    for ses in schedule:
        sesObj = {}
        sesObj['id'] = ses.id
        sesObj['datetime'] = ses.datetime
        sessionArray.append(sesObj)

    return jsonify({'slot': sessionArray})