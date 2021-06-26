from flask import Flask, render_template, request, redirect, session, url_for,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Quiz'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///User_db.sqlite'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Titanic.sqlite'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    FName = db.Column(db.String(80), nullable=False)
    LName = db.Column(db.String(120), nullable=False)
    Email = db.Column(db.Integer, nullable=False)
    Password = db.Column(db.String(80), nullable=False)
    Address = db.Column(db.String(120), nullable=False)
    City = db.Column(db.Integer, nullable=False)
    State = db.Column(db.String(80), nullable=False)




class Passengers(db.Model):
    PassengerId = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80), nullable=False)
    Sex = db.Column(db.String(80), nullable=False)
    Age = db.Column(db.Float(40), primary_key=False)
    def __str__(self):
        return f'{self.id}. მგზავრის სახელია: {self.name}; მგზავრი არის:{self.sex}; მგზავრის ასაკია{self.age}'
all_movies = Passengers.query.all()
print(all_movies)


@app.route('/about')
def about():
    # all_movies = Passengers.query.all()
    # print(all_movies)
    return render_template('about.html', all_movies=all_movies)

@app.route('/')
def home():
    models = ['BMW', 'Audi', 'Mercedes-Benz' ]
    return render_template("index.html", page_info=about, mod=models)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        f = request.form['FName']
        l = request.form['LName']
        e = request.form['Email']
        p = request.form['Password']
        a = request.form['Address']
        c = request.form['City']
        s = request.form['State']
        if f=='' or l=='' or e=='' or p=='':
            flash('გთხოვთ შეავსოთ აუცილებელი ველები', 'error')
        else:
            u1 =User(FName=f, LName=l, Email=float(e), Password=float(p), Address=float(a), City=c, State=s)
            db.session.add(u1)
            db.session.commit()
            flash('მომზმარებლის ინფორმაცია წარმატებით დაემატა', 'info')
    return render_template('login.html')

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/base')
def base():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)
