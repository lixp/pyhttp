from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String,  ARRAY, JSON
from sqlalchemy.orm import sessionmaker
engine = create_engine('mysql://root:123456@localhost:3306/cms?charset=utf8', encoding='utf-8', echo=True)
Base = declarative_base()
DBSession = sessionmaker(bind=engine)


# class Student(Base):
#     __tablename__ = 'student'
#     __table_args__ = {'extend_existing': True}
#
#     student_no = Column(String(12), primary_key=True)
#     student_score = Column(String(512))
#
#
# list_hello = []
# session = DBSession()
# student = Student(student_no='P051510915', student_score=str(list_hello))
# session.add(student)
# session.commit()
# session.close()
