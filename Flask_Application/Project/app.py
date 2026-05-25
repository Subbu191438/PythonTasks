from flask import Flask, render_template, request, redirect
from data import students

app = Flask(__name__)


# ---------------- HOME ----------------
@app.route('/')
def home():
    return render_template("index.html", students=students)


# ---------------- ADD ----------------
@app.route('/add', methods=['GET', 'POST'])
def add_student():

    if request.method == 'POST':

        name = request.form['name']

        new_student = {
            "id": len(students) + 1,
            "name": name
        }

        students.append(new_student)

        return render_template("add.html", student=new_student)

    return render_template("add.html")


# ---------------- UPDATE ----------------
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_student(id):

    student = None

    for s in students:
        if s['id'] == id:
            student = s
            break

    if not student:
        return "Student Not Found"

    if request.method == 'POST':

        updated_name = request.form['name']
        student['name'] = updated_name

        return redirect('/')

    return render_template("update.html", student=student)


# ---------------- DELETE ----------------
@app.route('/delete/<int:id>')
def delete_student(id):

    for student in students:

        if student['id'] == id:
            students.remove(student)
            return render_template("delete.html", student=student)

    return "Student Not Found"


# ---------------- RUN ----------------
if __name__ == '__main__':
    app.run(debug=True)