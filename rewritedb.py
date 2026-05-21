from company import app, db
from datetime import date
from company.models import User, Agreement, Employee, Company

with app.app_context():
    db.drop_all()
    db.create_all()

    admin = User(email='admin@gmail.com', first_name='Admin')
    admin.set_password('admin123')

    viewer = User(email='viewer@gmail.com', first_name='viewer')
    viewer.set_password('viewer123')

    db.session.add(admin)
    db.session.add(viewer)

    company1 = Company(name='TechSoft Solutions')
    company2 = Company(name='Global Innovations')
    company3 = Company(name='DataSystems Ltd.')

    db.session.add(company1)
    db.session.add(company2)
    db.session.add(company3)

    employee1 = Employee(
        full_name='Іван Петренко',
        address='м. Київ, вул. Хрещатик, 25',
        phone='+380501234567',
        position='Розробник Python',
        salary=25000,
        work_start=date(2020, 5, 15)
    )

    employee2 = Employee(
        full_name='Марія Сидорова',
        address='м. Львів, вул. Франка, 12',
        phone='+380671234567',
        position='Менеджер проектів',
        salary=30000,
        work_start=date(2019, 3, 10)
    )

    employee3 = Employee(
        full_name='Олексій Коваленко',
        address='м. Одеса, вул. Дерибасівська, 7',
        phone='+380631234567',
        position='Аналітик даних',
        salary=28000,
        work_start=date(2021, 1, 20)
    )

    employee4 = Employee(
        full_name='Наталія Іваненко',
        address='м. Харків, вул. Сумська, 45',
        phone='+380501234568',
        position='Дизайнер UX/UI',
        salary=22000,
        work_start=date(2022, 6, 5)
    )

    db.session.add(employee1)
    db.session.add(employee2)
    db.session.add(employee3)
    db.session.add(employee4)

    agreement1 = Agreement(
        code='TS-2023-001',
        start_date=date(2023, 1, 15),
        end_date=date(2023, 12, 31),
        amount=150000,
        note='Розробка CRM системи',
        company=company1
    )

    agreement2 = Agreement(
        code='GI-2023-005',
        start_date=date(2023, 3, 1),
        end_date=date(2024, 2, 28),
        amount=200000,
        note='Консалтингові послуги',
        company=company2
    )

    agreement3 = Agreement(
        code='DS-2023-010',
        start_date=date(2023, 5, 10),
        end_date=date(2023, 11, 30),
        amount=120000,
        note='Аналіз даних для маркетингу',
        company=company3
    )

    db.session.add(agreement1)
    db.session.add(agreement2)
    db.session.add(agreement3)

    agreement1.employees.extend([employee1, employee2])
    agreement2.employees.extend([employee2, employee3])
    agreement3.employees.extend([employee1, employee3, employee4])

    db.session.commit()
