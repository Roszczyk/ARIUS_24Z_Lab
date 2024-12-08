from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone, time
from flask import Flask
import os
from pathlib import Path

from database_model import Student, Teacher, Lessons, Subjects, TeacherCalendar

os.chdir(Path(__file__).parent)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)

def students_working_days():
    lessons = db.session.query(Lessons).all()
    student_on_weekdays = []
    for lesson in lessons:
        if lesson.lesson_date.weekday() < 5: # 0-4 - poniedziałek-piątek
            student_on_weekdays.append(lesson.student)
    student_on_weekdays = set(student_on_weekdays)
    return len(student_on_weekdays)


def teachers_weekends():
    lessons = db.session.query(Lessons).all()
    teacher_on_weekend = []
    for lesson in lessons:
        if lesson.lesson_date.weekday() >= 5: # 0-4 - poniedziałek-piątek
            teacher_on_weekend.append(lesson.teacher)
    teacher_on_weekend = set(teacher_on_weekend)
    return len(teacher_on_weekend)


def student_most_lessons():
    lessons = db.session.query(Lessons).all()
    student_on_lesson = []
    for lesson in lessons:
        student_on_lesson.append(lesson.student)
    max_student = [None, 0]
    for student in set(student_on_lesson):
        current_count = student_on_lesson.count(student)
        if current_count > max_student[1]:
            max_student[0] = student
            max_student[1] = current_count
    chosen_student = db.session.query(Student).filter_by(student_id = max_student[0]).first().__dict__
    if "_sa_instance_state" in chosen_student.keys():
        chosen_student.pop("_sa_instance_state")
    return chosen_student
    

def subject_most_lessons():
    lessons = db.session.query(Lessons).all()
    taught_subject = []
    for lesson in lessons:
        taught_subject.append(lesson.subject)
    max_subject = [None, 0]
    for sub in set(taught_subject):
        current_count = taught_subject.count(sub)
        if current_count > max_subject[1]:
            max_subject[0] = sub
            max_subject[1] = current_count
    chosen_subject = db.session.query(Subjects).filter_by(subject_id = max_subject[0]).first()
    return dict({
        "subject_name" : chosen_subject.field,
        "quantity" : max_subject[1]
    })


def maths_lessons():
    maths = db.session.query(Subjects).filter_by(field = "matematyka").first()
    maths_lessons = db.session.query(Lessons).filter_by(subject = maths.subject_id).all()
    return len(maths_lessons)


def wednesday_lessons():
    lessons = db.session.query(Lessons).all()
    wednesdays = 0
    for lesson in lessons:
        if lesson.lesson_date.weekday() == 2:
            wednesdays = wednesdays + 1
    return wednesdays

def teacher_on_weekday(teacher_id, weekday):
    lessons = db.session.query(Lessons).all()
    lessons_count = 0
    for lesson in lessons:
        if lesson.lesson_date.weekday() == weekday \
                and lesson.teacher == teacher_id:
            lessons_count = lessons_count + 1
    return lessons_count

if __name__ == "__main__":
    with app.app_context():
        print(students_working_days())
        print(teachers_weekends())
        print(student_most_lessons())
        print(subject_most_lessons())
        print(maths_lessons())
        print(wednesday_lessons())
        print(teacher_on_weekday(1, 0))