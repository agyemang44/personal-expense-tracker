from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import date

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect('expenses.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db()
    expenses = conn.execute('SELECT * FROM expenses ORDER BY date DESC').fetchall()
    total = conn.execute('SELECT SUM(amount) as total FROM expenses').fetchone()['total'] or 0
    conn.close()
    return render_template('index.html', expenses=expenses, total=total)

@app.route('/add', methods=['POST'])
def add():
    conn = get_db()
    conn.execute('INSERT INTO expenses (category, amount, note, date) VALUES (?, ?, ?)',
                 (request.form['category'], request.form['amount'], request.form['note'], date.today()))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
