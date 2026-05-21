from flask import render_template, request, flash, redirect, url_for
from company import db
from company import app
from company.models import Agreement, Employee, User
from company.counter import visits_counter
from flask_login import login_user, login_required, logout_user, current_user

@app.route("/")
@app.route("/index")
@login_required
def index():
    count = visits_counter()
    return render_template('index.html', show_navbar=True, visit_count=count, user=current_user)

@app.route("/agreements")
@login_required
def agreements():
    all_agreements = Agreement.query.all()
    return render_template('agreements.html', show_navbar=True, agreements=all_agreements, user=current_user)

@app.route("/employee")
@login_required
def employee():
    all_employees = Employee.query.all()
    return render_template('employee.html', show_navbar=True, employees=all_employees, user=current_user)

@app.route("/company")
@login_required
def company():
    return render_template('company.html', show_navbar=True, user=current_user)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Пошта вже зайнята', category='error')
        elif len(email) < 4:
            flash('Електронна скринька повинна містити більше 3 символів', category='error')
        elif len(firstName) < 2:
            flash('Ім\'я повинне містити більше 1 символів', category='error')
        elif password1 != password2:
            flash('Паролі не збігаються', category='error')
        elif len(password1) < 5:
            flash('Паролі повинний містити більше 4 символів', category='error')
        else:
            new_user = User(email=email, first_name=firstName)
            new_user.set_password(password1)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Користувач зареєстрований!', category='success')
            return redirect(url_for('index'))
    return render_template('signup.html', show_navbar=False, user=current_user)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if user:
            if user.check_password(password):
                login_user(user, remember=True)
                flash('Авторизація пройшла успішно!', category='success')
                return redirect(url_for('index'))
            else:
                flash('Напрвильний пароль!', category='error')
        else: 
            flash('Такої пошти не інсує!', category='error')
    return render_template('login.html', show_navbar=False, user=current_user)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
