#!/usr/bin/env python3

from datetime import datetime

from sqlalchemy import (CheckConstraint, Column, DateTime, Index, Integer,
                        PrimaryKeyConstraint, String, UniqueConstraint,
                        create_engine, desc, func)
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    __table_args__ = (
        PrimaryKeyConstraint(
            'id',
            name='id_pk'),
        UniqueConstraint(
            'email',
            name='unique_email'),
        CheckConstraint(
            'grade BETWEEN 1 AND 12',
            name='grade_between_1_and_12')
    )

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    email = Column(String(55))
    grade = Column(Integer())
    birthday = Column(DateTime())
    enrolled_date = Column(DateTime(), default=datetime.now())

    def __repr__(self):
        return f"Student {self.id}: {self.name},  Grade {self.grade}"


if __name__ == '__main__':
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()


    albert_einstein = Student(
        name="Albert Einstein",
        email="albert.einstein@zurich.edu",
        grade=6,
        birthday=datetime(
            year=1879,
            month=3,
            day=14
        ),
    )

    alan_turing = Student(
        name="Alan Turing",
        email="alan.turing@sherborne.edu",
        grade=11,
        birthday=datetime(
            year=1912,
            month=6,
            day=23
        ),
    )

    session.add_all([albert_einstein,alan_turing])
    session.commit()

    # # print(f"New student ID is {albert_einstein.id}.")
    # # print(f"New student ID is {alan_turing.id}.")

    # # students= (session.query(Student.name).all()) #returns all as per the repr
    # # print  ([student for student in students])

    # ####Order by. add Desc or ASC
    # stud_by_name=session.query(Student.name).order_by(desc(Student.name)).limit(1).all()
    # #print(stud_by_name)

    
   

    # session.query(Student).update({Student.grade:Student.grade+1})
    # print([(student.name, student.grade) for student in session.query(Student)])

    # session.delete()
    # students= (session.query(Student.name).all()) #returns all as per the repr
    # print  ([student for student in students])
    stud=session.query((Student)).filter(Student.id==1)
    
    albert=stud.first()

    ##delete
    session.delete(albert)
    session.commit()

    albert=stud.first()
    print(albert)



    # query = session.query(
    #     Student).filter(
    #         Student.name == "Albert Einstein")        

    # # retrieve first matching record as object
    # albert_einstein = query.first()

    # # delete record
    # session.delete(albert_einstein)
    # session.commit()

    # # try to retrieve deleted record
    # albert_einstein = query.first()

    # print(albert_einstein)