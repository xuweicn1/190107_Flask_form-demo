from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField,PasswordField

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'SECRET'

class LoginForm(Form):
    # username = StringField('Name:', validators=[validators.required()])
    # password = PasswordField('Password:', validators=[validators.required()])
    s = StringField('设置：')
    v = StringField('值：')

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])

@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
    if request.method == 'POST' and form.validate():
        name=request.form['name']
        print(name)
        flash('修改成功', 'success')
    return render_template('hello1.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        name=request.form['username']
        password = request.form['password']
        print(name)
        print(password)
    return render_template('login.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)