import sys
import os
from pathlib import Path
from datetime import datetime, timedelta

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

os.chdir(Path(__file__).parent)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False
db = SQLAlchemy()
db.init_app(app)

from data_classes import Student, Teacher, Lessons, Subjects, TeacherCalendar


@app.route('/teacher-list', methods=['GET'])
def get_teacher_list():
    teachers = db.session.query(Teacher).all()
    return jsonify([{
        'id': teacher.teacher_id,
        'imie': teacher.name,
        'nazwisko': teacher.surname,
        'przedmioty' : [x.field for x in teacher.subjects]
    } for teacher in teachers])


@app.route('/teacher-details/<int:id>', methods=['GET'])
def get_teacher_details(id):
    teacher = db.session.query(Teacher).filter_by(teacher_id=id).first()
    if teacher:
        return jsonify({
            'imie': teacher.name,
            'nazwisko': teacher.surname,
            'przedmioty' : [x.field for x in teacher.subjects],
            'opis': teacher.description,
            'ocena': teacher.grade,
            'telefon': teacher.phone,
            'stawka': teacher.earnings,
            'waluta': teacher.currency,
            'email': teacher.email,
            'kalendarz' : {
                "od" : db.session.query(TeacherCalendar).filter_by(teacher=teacher.teacher_id).first().available_from.strftime("%H:%M"),
                "do" : db.session.query(TeacherCalendar).filter_by(teacher=teacher.teacher_id).first().available_to.strftime("%H:%M")
            }
        })
    else:
        return jsonify({'error': 'Brak rekordu'}), 404
    

@app.route('/book-lesson', methods=['POST'])
def book_lesson():
    data = request.get_json()
    student_id = data.get('student-id')
    teacher_id = data.get('teacher-id')
    when = datetime.strptime(data.get('when'), '%Y-%m-%d %H:%M')
    subject_id = data.get('subject-id')

    teacher = db.session.query(Teacher).filter_by(teacher_id=teacher_id).first()

    # sprawdzenie czy dany nauczyciel naucza podanego przedmiotu
    if subject_id not in [x.subject_id for x in teacher.subjects]:
        return jsonify({'Error': f'Nauczyciel {teacher.name} {teacher.surname} nie naucza {db.session.query(Subjects).filter_by(subject_id = subject_id).first().field}'}), 400
    
    # sprawdzenie czy dany nauczyciel pracuje w podanym terminie
    teacher_calendar = db.session.query(TeacherCalendar).filter_by(teacher=teacher_id).first()
    if when.time() < teacher_calendar.available_from or (when - timedelta(hours=1)).time() >= teacher_calendar.available_to:
        return jsonify({'Error': f'{teacher.name} {teacher.surname} pracuje w godzinach {teacher_calendar.available_from} - {teacher_calendar.available_to}'}), 400
    
    # sprawdzenie czy dany wskazany termin jest zarezerwowany
    lessons = db.session.query(Lessons).filter_by(teacher=teacher_id, lesson_date = when).all()
    if lessons:
        return jsonify({'Error': f'Podany termin ({when}) jest juz zarezerwowany'}), 400
    
    db.session.add(Lessons(lesson_date=when, teacher_id=teacher_id, subject_id=subject_id, student_id=student_id))
    db.session.commit()

    return jsonify({'message': 'Rezerwacja zakonczona sukcesem!'}), 201


@app.route('/add-teacher', methods=['POST'])
def add_teacher():
    data = request.get_json()
    for i in ['name', 'surname', 'description', 'grade', 'phone', 'earnings', 'currency', 'email', 'subjects', 'from', 'to']:
        if i not in data:
            return jsonify({'Error': f'Brak podanego argumentu - {i}'}), 400
    name = data.get('name')
    surname = data.get('surname')
    description = data.get('description')
    grade = float(data.get('grade'))
    if grade > 5 or grade < 1:
        return jsonify({'Error': f'Grade musi byc w zakresie <1,5>'}), 400
    phone = data.get('phone')
    earnings = int(data.get('earnings'))
    currency = data.get('currency')
    email = data.get('email')
    subjects = data.get('subjects').split(",")
    works_from = datetime.strptime(data.get('from'), '%H:%M')
    works_to = datetime.strptime(data.get('to'), '%H:%M')

    subjects_list = [db.session.query(Subjects).filter_by(subject_id = int(x)).first() for x in subjects]

    if db.session.query(Teacher).filter_by(name=name, surname=surname, email=email).all():
        return jsonify({'Error': f'{name} {surname} juz istnieje'}), 400

    teacher = Teacher(
        name=name, surname=surname, description=description,
        grade=grade, phone=phone, earnings=earnings, currency=currency, email=email,
        subjects=subjects_list
    )
    db.session.add(teacher)

    teacher_id = db.session.query(Teacher).filter_by(name=name, surname=surname, description=description,
        grade=grade, phone=phone, earnings=earnings, currency=currency, email=email).first().teacher_id
    
    db.session.add(TeacherCalendar(teacher=teacher_id, available_from=works_from.time(), available_to=works_to.time()))
    db.session.commit()
    
    return jsonify({'message': f'Nauczyciel {name} {surname} dodany. Teacher ID: {teacher_id}'}), 201


@app.route('/get-lessons', methods=['GET'])
def get_student_lessons():
    for i in ['student_id', "check_from", "check_to"]:
        if i not in request.args:
            return jsonify({'Error': f'Brak podanego argumentu - {i}'}), 400
    student_id = request.args.get('student_id')
    check_from = request.args.get('check_from')
    check_to = request.args.get('check_to')
    lessons = db.session.query(Lessons).filter_by(student=student_id).all()
    check_from = datetime.strptime(check_from, '%Y-%m-%d %H:%M')
    check_to = datetime.strptime(check_to, '%Y-%m-%d %H:%M')
    chosen_lessons = []
    for lesson in lessons:
        if lesson.lesson_date < check_to and lesson.lesson_date > check_from:
            chosen_lessons.append(lesson)

    def teacher_name_finder(teacher_id):
        teacher = db.session.query(Teacher).filter_by(teacher_id=teacher_id).first()
        return f"{teacher.name} {teacher.surname}"
    
    return jsonify([{
        'id': lesson.lesson_id,
        'data': lesson.lesson_date,
        'id_nauczyciela' : lesson.teacher,
        'nauczyciel': teacher_name_finder(lesson.teacher),
        'przedmiot' : db.session.query(Subjects).filter_by(subject_id=lesson.subject).first().field
    } for lesson in chosen_lessons])


if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)