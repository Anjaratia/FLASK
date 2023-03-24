from flask import Flask, g, redirect, session, render_template, request, url_for
import sqlite3
import pandas as pd
import os
from werkzeug.utils import secure_filename

class User:
    def __init__(self, id, user_id, password, units):
        self.id = id
        self.user_id = user_id
        self.password = password
        self.units = units

    def __repr__(self):
        return f'<User: {self.user_id}>'

class Unit:
    def __init__(self, name, se_form_url, pe_form_url):
        self.name = name
        self.se_form_url = se_form_url
        self.pe_form_url = pe_form_url

ict302 = Unit(name='ICT302',
              se_form_url='Self Evaluation Form',
              pe_form_url='Peer evaluation Form')

users = []
users.append(User(id=1, user_id='110001', password='ciao5', units=[ict302]))

users.append(User(id=2, user_id='220001', password='sprinklr', units=[ict302]))
users.append(User(id=3, user_id='220002', password='moon450', units=[ict302]))

users.append(User(id=4, user_id='330001', password='jackson5', units=[ict302]))
users.append(User(id=5, user_id='330002', password='applepie', units=[ict302]))
users.append(User(id=6, user_id='330003', password='bobsburgers', units=[ict302]))
users.append(User(id=7, user_id='330004', password='33strike', units=[ict302]))
users.append(User(id=8, user_id='330005', password='diary101', units=[ict302]))
users.append(User(id=9, user_id='330006', password='passss', units=[ict302]))
users.append(User(id=10, user_id='330007', password='worddd', units=[ict302]))
users.append(User(id=11, user_id='330008', password='elephantsrock', units=[ict302]))
users.append(User(id=12, user_id='330009', password='studyhard89', units=[ict302]))
users.append(User(id=13, user_id='330010', password='invalid', units=[ict302]))
users.append(User(id=14, user_id='330011', password='livelaughlove', units=[ict302]))
users.append(User(id=15, user_id='330012', password='jblover', units=[ict302]))
users.append(User(id=16, user_id='330013', password='5ever', units=[ict302]))
users.append(User(id=17, user_id='330014', password='wintersnow', units=[ict302]))
users.append(User(id=18, user_id='330015', password='zeldachampion', units=[ict302]))

app = Flask(__name__)
app.secret_key = 'turnkeytechnologies'

@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user


def upload_excel(file_path):
    df = pd.read_excel(file_path)
    conn = sqlite3.connect('database.db')
    df.to_sql('students', conn, if_exists='append', index=False)
    conn.close()

@app.route('/upload', methods=['POST'])
def upload_students():
    file = request.files['file']
    if file.filename.endswith('.xlsx'):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
        file.save(file_path)
        upload_students_from_excel(file_path)
        return 'File uploaded successfully!'
    else:
        return 'Invalid file format!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        user_id = request.form['user_id']
        password = request.form['password']
        
        user = [x for x in users if x.user_id == user_id][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))

        return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if not g.user:
        return redirect(url_for('login'))

    units = g.user.units
    return render_template('dashboard.html', units=units)

@app.route('/students')
def student_home():
    return render_template('student_home.html')

@app.route('/unit_coordinators')
def coordinator_home():
    return render_template('uc_home.html')

@app.route('/admin')
def admin_home():
    return render_template('admin.html')

@app.route('/self_evaluation', methods=['GET', 'POST'])
def self_evaluation():
    if request.method == 'POST':
        return redirect(url_for('student_home'))
    else:
        return render_template('se.html')

@app.route('/peer_evaluation', methods=['GET', 'POST'])
def peer_evaluation():
    if request.method == 'POST':
        return redirect(url_for('student_home'))
    else:
        return render_template('pe.html')

def calculate_score(form1, form2):
    score = 0
    common_keys = set(form1.keys()) & set(form2.keys())
    for key in common_keys:
        score += int(form1[key]) + int(form2[key])
    return score

@app.route('/results')
def results():
    form1 = session.get('se_form1', {})
    form2 = session.get('se_form2', {})
    if not form1 or not form2:
        return redirect(url_for('self_evaluation'))
    score = calculate_score(form1, form2)
    return render_template('result.html', score=score)

if __name__ == '__main__':
    app.run(debug=True)