from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///class_schedule.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class course(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    number = db.Column(db.String(500), nullable=False)
    max_numb_of_students = db.Column(db.String(3), nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.name}"

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method=='POST':
        name = request.form['name']
        number = request.form['number']
        max_numb_of_students = request.form['max_numb_of_students']
        todo = course(name=name, number=number, max_numb_of_students=max_numb_of_students)
        db.session.add(todo)
        db.session.commit()
        
    allcourse = course.query.all()
    return render_template('index.html', allcourse=allcourse)

@app.route('/show')
def products():
    allcourse = course.query.all()
    print(allcourse)
    return 'this is courses page'

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method=='POST':
        name = request.form['name']
        number = request.form['number']
        max_numb_of_students = request.form['max_numb_of_students']
        todo = course.query.filter_by(sno=sno).first()
        todo.name = name
        todo.number = number
        todo.max_numb_of_students = max_numb_of_students
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
        
    todo = course.query.filter_by(sno=sno).first()
    return render_template('update.html', todo=todo)

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = course.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

class instructor(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    number = db.Column(db.String(500), nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.name}"

@app.route('/form2', methods=['GET', 'POST'])
def helloworld2():
    if request.method=='POST':
        name = request.form['name']
        number = request.form['number']
        todo = instructor(name=name, number=number)
        db.session.add(todo)
        db.session.commit()
        
    allinstructor = instructor.query.all() 
    return render_template('form2.html', allinstructor=allinstructor)

@app.route('/show2')
def products2():
    allinstructor = instructor.query.all()
    print(allinstructor)
    return 'this is instructor page'

@app.route('/update2/<int:sno>', methods=['GET', 'POST'])
def update2(sno):
    if request.method=='POST':
        name = request.form['name']
        number = request.form['number']
        todo = instructor.query.filter_by(sno=sno).first()
        todo.name = name
        todo.number = number
        db.session.add(todo)
        db.session.commit()
        return redirect("/form2")
        
    todo = instructor.query.filter_by(sno=sno).first()
    return render_template('update2.html', todo=todo)

@app.route('/delete2/<int:sno>')
def delete2(sno):
    todo = instructor.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/form2")

class dept(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.name}"

@app.route('/form3', methods=['GET', 'POST'])
def helloworld3():
    if request.method=='POST':
        name = request.form['name']
        todo = dept(name=name)
        db.session.add(todo)
        db.session.commit()
        
    alldept = dept.query.all() 
    return render_template('form3.html', alldept=alldept)

@app.route('/show3')
def products3():
    alldept = dept.query.all()
    print(alldept)
    return 'this is departments page'

@app.route('/update3/<int:sno>', methods=['GET', 'POST'])
def update3(sno):
    if request.method=='POST':
        name = request.form['name']
        todo = dept.query.filter_by(sno=sno).first()
        todo.name = name
        db.session.add(todo)
        db.session.commit()
        return redirect("/form3")
        
    todo = dept.query.filter_by(sno=sno).first()
    return render_template('update3.html', todo=todo)

@app.route('/delete3/<int:sno>')
def delete3(sno):
    todo = dept.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/form3")

class meeting_time(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(200), nullable=False)
    id = db.Column(db.String(200), nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.time}"

@app.route('/form4', methods=['GET', 'POST'])
def helloworld4():
    if request.method=='POST':
        time = request.form['time']
        id = request.form['id']
        todo = meeting_time(time=time, id=id)
        db.session.add(todo)
        db.session.commit()
        
    allmeeting_time = meeting_time.query.all() 
    return render_template('form4.html', allmeeting_time=allmeeting_time)

@app.route('/show4')
def products4():
    allmeeting_time = meeting_time.query.all()
    print(allmeeting_time)
    return 'this is slots page'

@app.route('/update4/<int:sno>', methods=['GET', 'POST'])
def update4(sno):
    if request.method=='POST':
        time = request.form['time']
        id = request.form['id']
        todo = dept.query.filter_by(sno=sno).first()
        todo.time = time
        todo.id = id
        db.session.add(todo)
        db.session.commit()
        return redirect("/form4")
        
    todo = meeting_time.query.filter_by(sno=sno).first()
    return render_template('update4.html', todo=todo)

@app.route('/delete4/<int:sno>')
def delete4(sno):
    todo = meeting_time.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/form4")

class room(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(200), nullable=False)
    capacity = db.Column(db.String(200), nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.number}"

@app.route('/form5', methods=['GET', 'POST'])
def helloworld5():
    if request.method=='POST':
        number = request.form['number']
        capacity = request.form['capacity']
        todo = room(number=number, capacity=capacity)
        db.session.add(todo)
        db.session.commit()
        
    allroom = room.query.all() 
    return render_template('form5.html', allroom=allroom)

@app.route('/show5')
def products5():
    allroom = room.query.all()
    print(allroom)
    return 'this is rooms page'

@app.route('/update5/<int:sno>', methods=['GET', 'POST'])
def update5(sno):
    if request.method=='POST':
        number = request.form['number']
        capacity = request.form['capacity']
        todo = room.query.filter_by(sno=sno).first()
        todo.number = number
        todo.capacity = capacity
        db.session.add(todo)
        db.session.commit()
        return redirect("/form5")
        
    todo = room.query.filter_by(sno=sno).first()
    return render_template('update5.html', todo=todo)

@app.route('/delete5/<int:sno>')
def delete5(sno):
    todo = room.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/form5")

class dept_course(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    course_numb = db.Column(db.String(200), nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.name}"

@app.route('/form6', methods=['GET', 'POST'])
def helloworld6():
    if request.method=='POST':
        name = request.form['name']
        course_numb = request.form['course_numb']
        todo = dept_course(name=name, course_numb=course_numb)
        db.session.add(todo)
        db.session.commit()
        
    alldept_course = dept_course.query.all() 
    return render_template('form6.html', alldept_course=alldept_course)

@app.route('/show6')
def products6():
    alldept_course = dept_course.query.all()
    print(alldept_course)
    return 'this is department-->course page'

@app.route('/update6/<int:sno>', methods=['GET', 'POST'])
def update6(sno):
    if request.method=='POST':
        name = request.form['name']
        course_numb = request.form['course_numb']
        todo = dept_course.query.filter_by(sno=sno).first()
        todo.name = name
        todo.course_numb = course_numb
        db.session.add(todo)
        db.session.commit()
        return redirect("/form6")
        
    todo = dept_course.query.filter_by(sno=sno).first()
    return render_template('update6.html', todo=todo)

@app.route('/delete6/<int:sno>')
def delete6(sno):
    todo = dept_course.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/form6")

class course_instructor(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    course_number = db.Column(db.String(200), nullable=False)
    instructor_number = db.Column(db.String(200), nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.course_number}"

@app.route('/form7', methods=['GET', 'POST'])
def helloworld7():
    if request.method=='POST':
        course_number = request.form['course_number']
        instructor_number = request.form['instructor_number']
        todo = course_instructor(course_number=course_number, instructor_number=instructor_number)
        db.session.add(todo)
        db.session.commit()
        
    allcourse_instructor = course_instructor.query.all() 
    return render_template('form7.html', allcourse_instructor=allcourse_instructor)

@app.route('/show7')
def products7():
    allcourse_instructor = course_instructor.query.all()
    print(allcourse_instructor)
    return 'this is course-->instructor page'

@app.route('/update7/<int:sno>', methods=['GET', 'POST'])
def update7(sno):
    if request.method=='POST':
        course_number = request.form['course_number']
        instructor_number = request.form['instructor_number']
        todo = course_instructor.query.filter_by(sno=sno).first()
        todo.course_number = course_number
        todo.instructor_number = instructor_number
        db.session.add(todo)
        db.session.commit()
        return redirect("/form7")
        
    todo = course_instructor.query.filter_by(sno=sno).first()
    return render_template('update7.html', todo=todo)

@app.route('/delete7/<int:sno>')
def delete7(sno):
    todo = course_instructor.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/form7")

@app.route('/generate', methods=['GET', 'POST'])
def gen():
    return render_template("generate.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)