from sqlalchemy import func, desc
from models import Student, Grade, Subject, Group, Teacher
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine("sqlite:///mynotes.dbS")
Session = sessionmaker(bind=engine)
session = Session()

# Знайти середній бал на потоці 
def select_4():
    average_grade = session.query(func.avg(Grade.grade).label('average_grade')).scalar()
     