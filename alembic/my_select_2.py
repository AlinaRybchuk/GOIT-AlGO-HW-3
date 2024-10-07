from sqlalchemy import func, desc
from models import Student, Grade, Subject, Group, Teacher
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///mynotes.dbS")
Session = sessionmaker(bind=engine)
session = Session()

# Знайти студента із найвищим середнім балом з певного предмета
def select_2():
    result = session.query(Student.fullname, func.avg(Grade.grade).label('average_grade'))\
     .join(Grade).filter(Grade.subject_id == Grade.subject_id).group_by(Student.id).order_by(func.avg(Grade.grade).desc()).limit(1).all()