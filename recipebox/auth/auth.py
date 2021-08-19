from flask import render_template, request, url_for, redirect, flash
from flask_login import login_user, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from recipebox import db
from recipebox.models.auth import User
from . import auth_bp


@auth_bp.route('/register/')
def register():
    return render_template('register.html')


@auth_bp.route('/register/', methods=['POST'])
def register_post():
    # validate and add to db here
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    if user:
        flash('Email address already exists')
        return redirect(url_for('auth_bp.register'))

    new_user = User(
        email=email,
        username=username,
        password=generate_password_hash(password)
    )

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth_bp.login'))


@auth_bp.route('/login/')
def login():
    return render_template('login.html')


@auth_bp.route('/login/', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth_bp.login'))

    login_user(user, remember=False)
    return redirect(url_for('auth_bp.profile'))


@auth_bp.route('/profile/')
@login_required
def profile():
    return render_template('profile.html', user=current_user)


@login_required
@auth_bp.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('auth_bp.login'))
