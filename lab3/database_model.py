from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone, time
from flask import Flask
import os
from pathlib import Path

os.chdir(Path(__file__).parent)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)

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


def fill_database():
    # wyczyszczenie poprzednio dodanych do bazy danych elementów (na wszelki wypadek)
    db.session.query(Lessons).delete()
    db.session.query(TeacherCalendar).delete()
    db.session.query(Teacher).delete()
    db.session.query(Student).delete()
    db.session.query(Subjects).delete()

    # PRZEDMIOTY:
    math = Subjects(field = 'matematyka')
    physics = Subjects(field = 'fizyka')
    chemistry = Subjects(field = 'chemia')
    history = Subjects(field = "historia")
    wos = Subjects(field = "WoS")
    geography = Subjects(field = "geography")
    biology = Subjects(field = 'biologia')
    db.session.add_all([math, physics, chemistry, history, wos, geography, biology])

    # NAUCZYCIELE:
    teacher1 = Teacher(
        name='Anna', surname='Kowalska', description='nauczyciel szkoły podstawowej',
        grade=4.5, phone='123456789', earnings=50, currency='PLN', email='anna@example.com',
        subjects=[math, physics]
    )
    teacher2 = Teacher(
        name='Jan', surname='Nowak', description='student medycyny', 
        grade=4.0, phone='987654321', earnings=60, currency='PLN', email='jan@example.com',
        subjects=[chemistry, biology]
    )
    teacher3 = Teacher(
        name='Walter', surname='White', description='nauczyciel chemii i biznesmen', 
        grade=5.0, phone='666666666', earnings=100, currency='USD', email='ww@heisenberg.com',
        subjects=[chemistry]
    )
    teacher4 = Teacher(
        name='Kazimiera', surname='Solejuk', description='filozof', 
        grade=4.5, phone='+48616564165', earnings=45, currency='PLN', email='solejukowa@ranczo.pl',
        subjects=[wos, history]
    )
    teacher5 = Teacher(
        name='Patrycja', surname='Dąbrowska', description='studentka geografii i geodezji', 
        grade=4.0, phone='+41555666777', earnings=100, currency='PLN', email='patrycja@example.com',
        subjects=[geography, biology]
    )
    db.session.add_all([teacher1, teacher2, teacher3, teacher4, teacher5]) 

    # STUDENCI:
    students = [
        Student(name="Jan", surname="Nowak", email="jan.nowak@example.com"),
        Student(name="Anna", surname="Kowalska", email="anna.kowalska@example.com"),
        Student(name="Tomasz", surname="Wiśniewski", email="tomasz.wisniewski@example.com")
    ]
    db.session.add_all(students)

    # GRAFIKI:
    schedules = [
        TeacherCalendar(teacher=1, available_from=time(9,0), available_to=time(17,0)), 
        TeacherCalendar(teacher=2, available_from=time(8,0), available_to=time(19,0)), 
        TeacherCalendar(teacher=3, available_from=time(14,0), available_to=time(20,0)),
        TeacherCalendar(teacher=4, available_from=time(8,0), available_to=time(13,0)), 
        TeacherCalendar(teacher=5, available_from=time(8,0), available_to=time(14,0))  
    ]
    db.session.add_all(schedules)

    # LEKCJE:
    lessons = [
        Lessons(lesson_date=datetime(2024, 12, 9, 10, 0), teacher_id=1, subject_id=1, student_id=1), 
        Lessons(lesson_date=datetime(2024, 12, 9, 12, 0), teacher_id=1, subject_id=2, student_id=1),  
        Lessons(lesson_date=datetime(2024, 12, 10, 14, 0), teacher_id=2, subject_id=1, student_id=1), 
        Lessons(lesson_date=datetime(2024, 12, 10, 11, 0), teacher_id=1, subject_id=2, student_id=2), 
        Lessons(lesson_date=datetime(2024, 12, 11, 9, 0), teacher_id=3, subject_id=1, student_id=2), 
        Lessons(lesson_date=datetime(2024, 12, 12, 13, 0), teacher_id=2, subject_id=3, student_id=2),  
        Lessons(lesson_date=datetime(2024, 12, 12, 15, 0), teacher_id=3, subject_id=1, student_id=2), 
        Lessons(lesson_date=datetime(2024, 12, 13, 10, 0), teacher_id=2, subject_id=2, student_id=2),  
        Lessons(lesson_date=datetime(2024, 12, 14, 12, 0), teacher_id=4, subject_id=1, student_id=3), 
        Lessons(lesson_date=datetime(2024, 12, 15, 11, 0), teacher_id=4, subject_id=3, student_id=3),  
        Lessons(lesson_date=datetime(2024, 12, 16, 10, 0), teacher_id=1, subject_id=1, student_id=1),  
        Lessons(lesson_date=datetime(2024, 12, 17, 11, 0), teacher_id=5, subject_id=2, student_id=2),  
        Lessons(lesson_date=datetime(2024, 12, 17, 12, 0), teacher_id=2, subject_id=3, student_id=2), 
        Lessons(lesson_date=datetime(2024, 12, 18, 10, 0), teacher_id=1, subject_id=2, student_id=1), 
        Lessons(lesson_date=datetime(2024, 12, 18, 13, 0), teacher_id=2, subject_id=1, student_id=2)  
    ]
    db.session.add_all(lessons)

    db.session.commit()




if __name__ == "__main__":
    if os.path.exists('instance/database.db'):
        # przy zmianach w modelu danych, istnienie poprzedniej bazy danych przeszkadza
        # wobec tego jest poprzednia instancja usuwana
        os.remove('instance/database.db')
    with app.app_context():
        db.create_all()
        fill_database()
    