from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from flask import Flask, render_template
from wtforms.validators import DataRequired, Email, Length
from wtforms import StringField, PasswordField, SubmitField

app = Flask(__name__)
app.secret_key = 'stringforcsrfsecurityflask'
bootstrap_base = Bootstrap5(app)

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(8)])
    submit = SubmitField(label='Log In')

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == 'admin@email.com' and login_form.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html', form=login_form)

    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)