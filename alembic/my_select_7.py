from sqlalchemy import func, desc
from models import Student, Grade, Subject, Group, Teacher
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///mynotes.dbS")
Session = sessionmaker(bind=engine)
session = Session()

# Знайти оцінки студентів у окремій групі з певного предмета
def select_7():
    grades = session.query(Grade.grades).join(Student, Grade.student_id == Student.id).filter(Student.group_id, Grade.subject_id).all()