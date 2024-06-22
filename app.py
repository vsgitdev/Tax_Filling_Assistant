from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    income = request.form['income']
    expenses = request.form['expenses']
    return f"Income: {income}, Expenses: {expenses}"

if __name__ == '__main__':
    app.run(debug=True)
