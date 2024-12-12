from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone, time
from flask import Flask

app = Flask(__name__)
db = SQLAlchemy()

teacher_subject_association = db.Table(
    'teacher_subjects',
    db.Column('teacher_id', db.Integer, db.ForeignKey('teachers.teacher_id'), nullable=False),
    db.Column('subject_id', db.Integer, db.ForeignKey('subjects.subject_id'), nullable=False)
)


class Teacher(db.Model):
    __tablename__ = "teachers"
    teacher_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), nullable = False)
    surname = db.Column(db.String(128), nullable = False)
    description = db.Column(db.String(1000), nullable = False)
    grade = db.Column(db.Float, nullable = False)
    phone = db.Column(db.String(12), nullable = False)
    earnings = db.Column(db.Integer, nullable = False)
    currency = db.Column(db.String(30), nullable = False)
    email = db.Column(db.String(128), nullable=False)
    subjects = db.relationship('Subjects', secondary='teacher_subjects', back_populates='teachers')

    def __init__(self, name, surname, description, grade, phone, earnings, currency, email, subjects):
        self.name = name
        self.surname = surname
        self.description = description
        self.grade = grade
        self.phone = phone
        self.earnings = earnings
        self.currency = currency
        self.email = email
        self.subjects = subjects


class Student(db.Model):
    __tablename__ = "students"
    student_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), nullable=False)
    surname = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)

    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email


class Subjects(db.Model):
    __tablename__ = "subjects"
    subject_id = db.Column(db.Integer, primary_key = True)
    field = db.Column(db.Integer, nullable = False)

    teachers = db.relationship('Teacher', secondary='teacher_subjects', back_populates='subjects')

    def __init__(self, field):
        self.field = field


class Lessons(db.Model):
    __tablename__ = "lessons"
    lesson_id = db.Column(db.Integer, primary_key = True)
    lesson_date = db.mapped_column(db.DateTime, default = datetime.now(timezone.utc))
    teacher = db.Column(db.Integer, db.ForeignKey("teachers.teacher_id"), nullable = False)
    subject = db.Column(db.Integer, db.ForeignKey("subjects.subject_id"), nullable = False)
    student = db.Column(db.Integer, db.ForeignKey("students.student_id"), nullable = False)

    def __init__(self, lesson_date, teacher_id, subject_id, student_id):
        self.lesson_date = lesson_date
        self.teacher = teacher_id
        self.subject = subject_id
        self.student = student_id


class TeacherCalendar(db.Model):
    __tablename__ = "calendar"
    calendar_id = db.Column(db.Integer, primary_key = True)
    teacher = db.Column(db.Integer, db.ForeignKey("teachers.teacher_id"), nullable = False)
    available_from = db.Column(db.Time, nullable=False)
    available_to = db.Column(db.Time, nullable=False)