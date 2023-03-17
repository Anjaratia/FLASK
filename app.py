from flask import Flask, g, redirect, render_template, request, session, url_for

class User:
    def __init__(self, id, user_id, password):
        self.id = id
        self.user_id = user_id
        self.password = password

    def __repr__(self):
        return f'<User: {self.user_id}>'

users = []
users.append(User(id=1, user_id='110001', password='ciao5'))

users.append(User(id=2, user_id='220001', password='sprinklr'))
users.append(User(id=3, user_id='220002', password='moon450'))

users.append(User(id=4, user_id='330001', password='jackson5'))
users.append(User(id=5, user_id='330002', password='applepie'))
users.append(User(id=6, user_id='330003', password='bobsburgers'))
users.append(User(id=7, user_id='330004', password='33strike'))
users.append(User(id=8, user_id='330005', password='diary101'))
users.append(User(id=9, user_id='330006', password='passss'))
users.append(User(id=10, user_id='330007', password='worddd'))
users.append(User(id=11, user_id='330008', password='elephantsrock'))
users.append(User(id=12, user_id='330009', password='studyhard89'))
users.append(User(id=13, user_id='330010', password='invalid'))
users.append(User(id=14, user_id='330011', password='livelaughlove'))
users.append(User(id=15, user_id='330012', password='jblover'))
users.append(User(id=16, user_id='330013', password='5ever'))
users.append(User(id=17, user_id='330014', password='wintersnow'))
users.append(User(id=18, user_id='330015', password='zeldachampion'))

app = Flask(__name__)
app.secret_key = 'turnkeytechnologies'

@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user
        

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

    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)