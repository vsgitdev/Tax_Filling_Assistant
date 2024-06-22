---------------------------------STEP 1----------------------------------
--------------Setup process and how to run the application---------------


---------Tax Filing Assistant----------

---Project Overview---

The Tax Filing Assistant is a simple web application developed using Flask to assist users with basic tax advice based on their input.
This application allows users to input their income and expenses and provides basic tax information tailored to their financial situation.



---Setup Instructions---




--Prerequisites--

Python 3.x

Virtual environment (Not necessarily needed but recommended)

Flask

Visual Studio Code (VS Code)



--Installation--

--Steps--

   1. Clone the repository:
      Run the following commands on the terminal:
        git clone https://github.com/vsgitdev/Tax_Filing_Assistant.git
        cd Tax_Filing_Assistant
   2. Create and activate a virtual environment: It's not necessary but it is recommended to create a virtual environment to manage dependencies.
      Run the following commands:
        python -m venv venv
        venv\Scripts\activate
   3. Install the required packages: With the virtual environment activated, install Flask using pip:
      Run the following commands:
       pip install Flask
   4. Create the app.py file with basic configuration and the launch.json file for debugging



--Run the Application (Using VSCode)--

--Steps--

1st way:
  1. Open VSCode and open terminal ( using ctrl + ~ ).
  2. Run the following command on the terminal to navigate to the project directory:
        cd Tax_Filing_Assistant
  3. Run the Flask application using the following command:
        python app.py     
  4. Open your web browser and go to:
        http://127.0.0.1:5000/


2st way:
   1. Open VSCode and press ctrl + shift + e
   2. Press Open Folder
   3. Choose the project folder and open it
   4. Open terminal ( using ctrl + ~ )
   5. Run the Flask application using the following command:
        python app.py     
   6. Open your web browser and go to:
        http://127.0.0.1:5000/


--Directory Structure--
Tax_Filing_Assistant/
├── __ pycache__/
├── .vscode/
│   └── launch.json
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── venv/
└── app.py


--Acknowledgements--

Font Awesome for the icons

Google Fonts for the fonts



------------------------STEP 2------------------------
---------Documentation of the API endpoints-----------

---------API Endpoints----------

--Submit Tax Information--
  URL: /submit
  Method: POST
Submits user-provided tax information (income and expenses) and validates the data.

Request
Data Params:
income: (numeric) User's income.
expenses: (numeric) User's expenses.

Responses
Success Response:
   Code: 201 Created
   Content:{ "message": "Data submitted successfully" }

Error Responses:
   Code: 400 Bad Request
   Content:
{ "error": "Invalid input. Please enter numeric values for income and    expenses" }
{ "error": "Income and expenses must not exceed 10 digits" }


--Success Page--
URL: /success
Method: GET
Displays a success message indicating the data was submitted correctly.

Responses
Success Response:
Code: 200 OK
Content: HTML page with success message.



Error Page
URL: /error
Method: GET
Displays an error message indicating the data submission failed.
Request


Query Params:
message: (string) The error message to display.
Responses
Error Response:
Code: 200 OK
Content: HTML page with error message.



---------------------------------STEP 3----------------------------------
--------------Explanation of how the AI model is integrated---------------

---Setup Instructions---




--Prerequisites--

Python 3.x

Flask

SQLAlchemy

OpenAI Python client library



--Installation--

--Steps--

1.Install dependencies running the following command:
    pip install flask sqlalchemy openai
2.Create a config.py file in the root directory of my project and add the provided OpenAI API key:
  # config.py
  OPENAI_API_KEY = 'your-openai-api-key'



--AI Integration--

--Steps--

1.Import necessary modules in app.py:
  from flask import Flask, render_template, request, redirect, url_for, jsonify
  from sqlalchemy import create_engine
  from sqlalchemy.orm import sessionmaker
  from database_setup import Base, TaxInfo
  import openai
  import config

2.Initialize Flask app and database connection:
  app = Flask(__name__)
  engine = create_engine('sqlite:///tax_info.db')
  Base.metadata.bind = engine
  DBSession = sessionmaker(bind=engine)
  session = DBSession()

3.Set OpenAI API key: 
  openai.api_key = config.OPENAI_API_KEY

4.Define route to handle form submission and generate AI advice:
   Generate AI Advice: The route sends a request to the OpenAI API (if the input data are correct/if validation is successful), including the user’s financial data. It prompts the AI to generate personalized tax advice based on the provided income and expenses.
   Process AI Response: The AI-generated advice is extracted from the API response and cleaned up if necessary.
   
5.Render AI advice in success.html to redirect the user to the success page where the AI-generated tax advice is displayed.:
  <div class="advice-container">
    <p>{{ advice }}</p>
   </div>
 
