from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, TaxInfo

app = Flask(__name__)

engine = create_engine('sqlite:///tax_info.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    income = request.form['income']
    expenses = request.form['expenses']
    
    # Server-side validation for numeric inputs and length
    try:
        income = float(income)
        expenses = float(expenses)
        
        if income <= 0 or expenses <= 0:
            return redirect(url_for('error', message="Income and expenses must be non-negative or zero"))
        if len(str(int(income))) > 10 or len(str(int(expenses))) > 10:
            return redirect(url_for('error', message="Income and expenses must not exceed 10 digits"))
    except ValueError:
        return redirect(url_for('error', message="Invalid input. Please enter numeric values for income and expenses"))

    new_tax_info = TaxInfo(income=str(income), expenses=str(expenses))
    session.add(new_tax_info)
    session.commit()
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/error')
def error():
    message = request.args.get('message', 'An error occurred')
    return render_template('error.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
