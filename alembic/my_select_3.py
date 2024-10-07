from sqlalchemy import func, desc
from models import Student, Grade, Subject, Group, Teacher
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///mynotes.dbS")
Session = sessionmaker(bind=engine)
session = Session()

# Знайти середній бал у групах з певного предмета
def select_3():
    average_grade = session.query(Group.name, func.avg(Grade.grade).label('average_grade'))\
     .join(Student, Group.id == Student.group_id).join(Grade, Student.id == Grade.student_id).filter(Grade.subject_id == Grade.subject_id).group_by(Group.id).all()