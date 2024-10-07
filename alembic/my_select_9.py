from sqlalchemy import func, desc
from models import Student, Grade, Subject, Group, Teacher
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///mynotes.dbS")
Session = sessionmaker(bind=engine)
session = Session()

#  Знайти список курсів, які відвідує певний студент
def select_9():
    courses = session.query(Subject.name).join(Grade, Subject.id == Grade.subject_id).filter(Grade.student_id).all()