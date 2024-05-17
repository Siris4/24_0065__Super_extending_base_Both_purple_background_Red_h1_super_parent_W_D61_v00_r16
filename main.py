# main.py
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import os

# Setting up environment variables before app initialization:

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('MYSECRETKEY', 'a_default_secret')  # This should be a secure, random key.

email = os.environ.get('MYSECRETUSERNAME', 'default-secret-username')

password = os.environ.get('MYSECRETPASSWORD', 'default-secret-password')


class MyLoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()], render_kw={"size": "30"})  # Email field with size attribute
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=4, max=30, message=None)], render_kw={"size": "30"})  # Password field with size attribute
    submit = SubmitField(label="Log In")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = MyLoginForm()
    if form.validate_on_submit():  # if a successful validation, then True
        if form.email.data == email and form.password.data == password:
            print(form.email.data)
            return redirect(url_for('success'))
        else:
            return redirect(url_for('denied'))
    else:
        # Form is not valid, print or log the errors
        print(form.errors)
    return render_template('login.html', form=form)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/denied')
def denied():
    return render_template('denied.html')

if __name__ == '__main__':
    app.run(debug=True)
