from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from faker import Faker

app = Flask(__name__)

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Password1@35.231.187.48/steph'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

fake = Faker()

class Hospital(db.Model):
    __tablename__ = 'hospitals'
    hospital_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hospital_name = db.Column(db.String(100), nullable=False)
    physicians = db.relationship('Physician', back_populates='hospital')
    patients = db.relationship('Patient', back_populates='hospital')

class Physician(db.Model):
    __tablename__ = 'physicians'
    physician_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hospital_id = db.Column(db.Integer, db.ForeignKey('hospitals.hospital_id'), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    date_of_registered_license = db.Column(db.Date)
    badge_id = db.Column(db.String(5))
    phone_number = db.Column(db.String(15))
    work_email = db.Column(db.String(100))

    hospital = db.relationship('Hospital', back_populates='physicians')

class Patient(db.Model):
    __tablename__ = 'patients'
    patient_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10))
    admission_date = db.Column(db.Date)
    phone_number = db.Column(db.String(15))
    email = db.Column(db.String(100))
    hospital_id = db.Column(db.Integer, db.ForeignKey('hospitals.hospital_id'))

    hospital = db.relationship('Hospital', back_populates='patients')

# Create the database tables within the application context
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def base():
    return render_template('base.html')

@app.route('/physicians')
def show_physicians():
    physicians = Physician.query.all()
    return render_template('physicians.html', data=physicians)

@app.route('/patients')
def show_patients():
    patients = Patient.query.all()
    return render_template('patients.html', data=patients)

if __name__ == '__main__':
    app.run(debug=True)
