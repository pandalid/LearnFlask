import os
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Length

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'HKHGgguihhjkhHkkGGkkgg'
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
db = SQLAlchemy(app)

bootstrap = Bootstrap(app)

#数据库
class User(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    phone = db.Column(db.String(11),unique=True)

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __repr__(self):
        return '<User %r>' % self.username

#表单
class LoginForm(FlaskForm):
    username = StringField('姓名',
                           validators = [DataRequired(message='请输入姓名')])
    phone = StringField('手机号', validators=[
                DataRequired(message= '手机号不能为空'), Length(11),])
    address = StringField('收件地址',
                  validators=[DataRequired(message= '请输入收件地址')])
    submit = SubmitField('提交')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/register',methods=['GET', 'POST'])
def register():
    form = LoginForm()
    if form.validate_on_submit():
        pass
    return render_template("register.html", form = form)


if __name__ == '__main__':
    app.run(host= '0.0.0.0')
