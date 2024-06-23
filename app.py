from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, TaxInfo
import openai
from dotenv import load_dotenv
import os

load_dotenv() 

app = Flask(__name__)

engine = create_engine('sqlite:///tax_info.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

openai.api_key = os.getenv('OPENAI_API_KEY')

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
        
        if income < 0 or expenses < 0:
            return redirect(url_for('error', message="Income and expenses must be non-negative"))
        if len(str(int(income))) > 10 or len(str(int(expenses))) > 10:
            return redirect(url_for('error', message="Income and expenses must not exceed 10 digits"))
    except ValueError:
        return redirect(url_for('error', message="Invalid input. Please enter numeric values for income and expenses"))

    new_tax_info = TaxInfo(income=str(income), expenses=str(expenses))
    session.add(new_tax_info)
    session.commit()

    # Call OpenAI API for tax advice
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a tax advisor."},
            {"role": "user", "content": f"Give me tax advice for an income of {income} and expenses of {expenses}."}
        ],
        max_tokens=150
    )
    tax_advice = response.choices[0].message['content'].strip()

    return redirect(url_for('success', advice=tax_advice))

@app.route('/success')
def success():
    advice = request.args.get('advice', 'No advice available')
    return render_template('success.html', advice=advice)

@app.route('/error')
def error():
    message = request.args.get('message', 'An error occurred')
    return render_template('error.html', message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
