from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    roll_no = db.Column(db.String(20), nullable=False, unique=True)
    college_name = db.Column(db.String(100), nullable=False)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        roll_no = request.form["roll_no"]
        college_name = request.form["college_name"]

        student = Student(name=name, roll_no=roll_no, college_name=college_name)
        db.session.add(student)
        db.session.commit()

        return "Registration successful!"
    with app.app_context():
        students = Student.query.all()
        print(students)
        return render_template("students.html", students=students)


if __name__ == "__main__":
    with app.app_context():
        # students = Student.query.all()

        db.create_all()
        student.query.all()
    app.run(debug=True, port=1234)
