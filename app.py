from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/students')
def student_home():
    return render_template('student_home.html')

@app.route('/unit_coordinators')
def coordinator_home():
    return render_template('uc_home.html')

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

@app.route('/results')
def results():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)