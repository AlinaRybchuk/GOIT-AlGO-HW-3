from sqlalchemy import func, desc
from models import Student, Grade, Subject, Group, Teacher
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///mynotes.dbS")
Session = sessionmaker(bind=engine)
session = Session()

# Знайти список студентів у певній групі
def select_6():
    list_of_students = session.query(Student.fullname).filter(Student.group_id).all()