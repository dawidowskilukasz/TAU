from datetime import datetime

from flask import Flask, render_template, redirect, url_for, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TimeField, DateField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    reservations = db.relationship('Reservation', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    place = db.Column(db.String(120), nullable=False)
    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    confirm_password = PasswordField('Potwierdź hasło', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Utwórz konto')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    submit = SubmitField('Zaloguj się')

class ReservationForm(FlaskForm):
    date = DateField('Data', validators=[DataRequired()])
    start_time = TimeField('Godzina rozpoczęcia', validators=[DataRequired()])
    end_time = TimeField('Godzina zakończenia', validators=[DataRequired()])
    submit = SubmitField('Zarezerwuj')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        if User.query.filter_by(email=email).first():
            flash('Podany adres email jest już zarejestrowany!', 'danger')
            return redirect(url_for('register'))

        new_user = User(email=email)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        flash('Utworzono konto! Możesz się teraz zalogować.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()

        if not user or not user.check_password(password):
            flash('Nieprawidłowy email lub hasło!', 'danger')
            return redirect(url_for('login'))

        login_user(user)
        flash('Zalogowano pomyślnie!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Wylogowano pomyślnie!', 'success')
    return redirect(url_for('index'))

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    places = ['Atlas Arena', 'Tauron Arena Kraków', 'Arena Gliwice']
    form = ReservationForm()

    if form.validate_on_submit():
        place = form.place.data
        date = form.date.data
        start_time = form.start_time.data
        end_time = form.end_time.data

        reservation = Reservation(
            user_id=current_user.id,
            place=place,
            date=date,
            start_time=start_time,
            end_time=end_time
        )

        db.session.add(reservation)
        db.session.commit()

        flash('Rezerwacja została dodana!', 'success')
        return redirect(url_for('dashboard'))

    user_reservations = current_user.reservations

    return render_template('dashboard.html', places=places, form=form, reservations=user_reservations)

@app.route('/reserved')
@login_required
def reserved():
    user_reservations = Reservation.query.filter_by(user_id=current_user.id).all()
    return render_template('reserved.html', reservations=user_reservations)

@app.route('/make_reservation/<place>', methods=['POST'])
@login_required
def make_reservation(place):
    date = request.form['date']
    start_time = request.form['start_time']
    end_time = request.form['end_time']

    reservation_date = datetime.strptime(date, '%Y-%m-%d').date()
    reservation_start_time = datetime.strptime(start_time, '%H:%M').time()
    reservation_end_time = datetime.strptime(end_time, '%H:%M').time()

    existing_reservation = Reservation.query.filter_by(place=place, date=reservation_date).first()
    if existing_reservation and (reservation_start_time < existing_reservation.end_time and reservation_end_time > existing_reservation.start_time):
        flash('Wybrane miejsce jest już zarezerwowane w tym terminie!', 'danger')
        return redirect(url_for('dashboard'))

    reservation = Reservation(
        user_id=current_user.id,
        place=place,
        date=reservation_date,
        start_time=reservation_start_time,
        end_time=reservation_end_time
    )

    db.session.add(reservation)
    db.session.commit()

    flash(f'Miejsce {place} zostało zarezerwowane na {date} od {start_time} do {end_time}.', 'success')
    return redirect(url_for('dashboard'))


@app.route('/edit_reservation/<reservation_id>', methods=['GET', 'POST'])
@login_required
def edit_reservation(reservation_id):
    reservation = Reservation.query.get_or_404(reservation_id)
    form = ReservationForm(obj=reservation)

    if form.validate_on_submit():
        form.populate_obj(reservation)
        db.session.commit()
        flash('Rezerwacja została zaktualizowana!', 'success')
        return redirect(url_for('reserved'))

    return render_template('edit_reservation.html', form=form, reservation=reservation)

    return redirect(url_for('reserved'))

@app.route('/cancel_reservation/<reservation_id>', methods=['POST'])
@login_required
def cancel_reservation(reservation_id):
    reservation = Reservation.query.get(reservation_id)

    if reservation.user_id != current_user.id:
        flash('Nie masz uprawnień do anulowania tej rezerwacji.', 'danger')
        return redirect(url_for('reserved'))

    db.session.delete(reservation)
    db.session.commit()
    flash('Rezerwacja została anulowana.', 'success')

    return redirect(url_for('reserved'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

