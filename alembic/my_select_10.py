from sqlalchemy import func, desc
from models import Student, Grade, Subject, Group, Teacher
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///mynotes.dbS")
Session = sessionmaker(bind=engine)
session = Session()

#  Список курсів, які певному студенту читає певний викладач.
def select_10():
    list_of_courses = session.query(Subject.name).join(Grade, Subject.id == Grade.subject_id).filter(Grade.student_id, Subject.teacher_id).all()

