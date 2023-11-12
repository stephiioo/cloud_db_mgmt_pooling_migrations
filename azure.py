"""

pip install sqlalchemy alembic mysql-connector-python pymysql

"""

## Part 1 - Define SQLAlchemy models for patients and their medical records:
### this file below could always be called db_schema.py or something similar

from sqlalchemy import create_engine, inspect, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Hospital(Base):
    __tablename__ = 'hospitals'

    hospital_id = Column(Integer, primary_key=True, autoincrement=True)
    hospital_name = Column(String(100), nullable=False)

class Physician(Base):
    __tablename__ = 'physicians'

    physician_id = Column(Integer, primary_key=True, autoincrement=True)
    hospital_id = Column(Integer, ForeignKey('hospitals.hospital_id'), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    date_of_registered_license = Column(Date)
    badge_id = Column(String(5))
    phone_number = Column(String(15))
    work_email = Column(String(100))

    hospital = relationship('Hospital', back_populates='physicians')

class Patient(Base):
    __tablename__ = 'patients'

    patient_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    gender = Column(String(10))
    admission_date = Column(Date)
    phone_number = Column(String(15))
    email = Column(String(100))
    hospital_id = Column(Integer, ForeignKey('hospitals.hospital_id'))

    hospital = relationship('Hospital', back_populates='patients')

# Additional relationship in Hospital class
Hospital.physicians = relationship('Physician', back_populates='hospital')
Hospital.patients = relationship('Patient', back_populates='hospital')




### Part 2 - initial sqlalchemy-engine to connect to db:

engine = create_engine("mysql+mysqlconnector://steph:Password1@mygration.mysql.database.azure.com/steph")

## Test connection

inspector = inspect(engine)
inspector.get_table_names()


### Part 3 - create the tables using sqlalchemy models, with no raw SQL required:

Base.metadata.create_all(engine)