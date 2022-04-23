from flask import Blueprint, render_template, redirect, url_for, request, jsonify
import flask_login

from models import Course, Session, Enrolled
from forms import ChoiceForm
from extension import db


bp2 = Blueprint('view', __name__)

@bp2.route('/user', methods=['GET', 'POST'])
def get_data():
    form = ChoiceForm()
    user = flask_login.current_user
    registered = user.student_course_session
    student_course = user.courses
    course_list = Course.query.all()

    form.option.query = [subject for subject in course_list if subject not in student_course]

    if form.validate_on_submit():  
        assoc = Enrolled(student=user, course=form.option.data, session=form.timeslot.data)

        db.session.add(assoc)
        db.session.commit()
        return redirect(url_for('view.get_data'))

    return render_template('user.html', form=form, registered=registered, user=user)


@bp2.route('/<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    course = Course.query.filter_by(id=id).first()
    user = flask_login.current_user

    if request.method == "POST":
        user.courses.remove(course)

        db.session.commit()
        return redirect('/user')
    
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