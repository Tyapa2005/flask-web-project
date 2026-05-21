from company import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

employee_agreement = db.Table('employee_agreement',
    db.Column('employee_id', db.Integer, db.ForeignKey('employee.id'), primary_key=True),
    db.Column('agreement_id', db.Integer, db.ForeignKey('agreement.id'), primary_key=True)
)

class User(db.Model, UserMixin):
    """ Користувачі """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username} ({self.role})>"

class Company(db.Model):
    """ Компанія, яка має договори """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    agreements = db.relationship('Agreement', backref='company', lazy=True)

    def __repr__(self):
        return f"<Company {self.name}>"

class Agreement(db.Model):
    """ Договір між компанією та працівниками """
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(50), unique=True, nullable=False)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    amount = db.Column(db.Float)
    note = db.Column(db.String(200))

    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)

    employees = db.relationship('Employee', secondary=employee_agreement, backref='agreements')

    def __repr__(self):
        return f"<Agreement {self.code} with {self.company.name}>"

class Employee(db.Model):
    """ Працівник, який може бути вказаний у кількох договорах """
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200))
    phone = db.Column(db.String(20))
    position = db.Column(db.String(100))
    salary = db.Column(db.Float)
    work_start = db.Column(db.Date)
    work_end = db.Column(db.Date)

    def __repr__(self):
        return f"<Employee {self.full_name}>"