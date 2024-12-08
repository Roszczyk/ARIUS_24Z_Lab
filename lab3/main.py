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
    pass

def maths_lessons():
    pass

def wednesday_lessons():
    pass

def teachers_list(teacher_id):
    pass


with app.app_context():
    print(students_working_days())
    print(teachers_weekends())
    print(student_most_lessons())