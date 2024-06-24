# tax_assistant
A tax filing assistant web application

---Project Overview---

The Tax Filing Assistant is a simple web application developed using Flask to assist users with basic tax advice based on their input.
This application allows users to input their income and expenses and provides basic tax information tailored to their financial situation.


# TASK 1
-----------Setup process and how to run the application-------------

---Setup Instructions---


--Prerequisites--

Python 3.x

Virtual environment (Not necessarily needed but recommended)

Flask

Visual Studio Code (VS Code)



--Installation--

--Steps--

  1. Open a Command Prompt on your computer or a terminal [ If u use VSCode IDE open terminal ( using ctrl + ~ )].

  2. Create the project repository by running the following command:
     mkdir tax_filing_assistant

  3. Run the following command on the terminal to navigate to the project directory:
        cd tax_filing_assistant

  4. Create and activate a virtual environment ( It's not necessary but it is recommended to create a virtual environment to manage dependencies.) by using these commands:
     python -m venv venv
     venv\Scripts\activate  # On Windows
     source venv/bin/activate  # On macOS/Linux

  5. Install the required packages : With the virtual environment activated, install Flask using pip with the following command:
     pip install Flask 



--Set up project process--

--Steps--

1. Create the app.py file with basic configuration and the launch.json file for debugging

2. Create the index.html file for the homepage the style.css for the homepage's styling and then added 2 more pages : success and error page for handling the messages and results provided to the user according to the inputs.


--Connection with github repository--

--Steps--

1.Create github repository

2.Initialize Git in your project directory running the following command:
  git init

3.Add all files to the repository running the following command:
  git add .

4.Commit the changes running the following command:
  git commit -m "Initial commit"

5.Push your local repository to GitHub:
  git remote add origin https://github.com/vsgitdev/Tax_Filling_Assistant.git
  git branch -M main
  git push -u origin main


  
--Run the Application (for someone who is not the creator of the app)--

--Steps--

  1. Open a Command Prompt on your computer or a terminal [ If you use VSCode IDE open terminal ( using ctrl + ~ )].

  2. Run the following command on the terminal to clone the project repository:
     https://github.com/vsgitdev/Tax_Filling_Assistant.git

  3. Run the following command on the terminal to navigate to the project directory:
        cd tax_filing_assistant

  4. Create and activate a virtual environment ( It's not necessary but it is recommended to create a virtual environment to manage dependencies.) by using these commands:
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux 
   
  5. Run the Flask application using the following command:
        python app.py     

  6. Open your web browser and go to:
        http://127.0.0.1:5000/


--Acknowledgements--

Font Awesome for the icons

Google Fonts for the fonts


# TASK 2
---------Documentation of the API endpoints-----------



--Installation of SQLite and Setup of database--

--Steps--

1. Install sqlalchemy package running the following command:
    pip install sqlalchemy

2. Install dependencies running the following command:
    pip install flask sqlalchemy openai (for the next step)

3. Create database_setup.py file which contains script that defines the database and the table structure. 

4. Run database_setup.py to create the database and this will create tax_info.db with the defined table structure using this command :
   python database_setup.py


---------API Endpoints----------

--Submit Tax Information--
  URL: /submit
  Method: POST
  This endpoint accepts tax information from the user, specifically their income   and expenses. The data is validated to ensure it is numeric and within acceptable limits.

Request
Data Parameters:
income: A numeric value representing the user's income.
expenses: A numeric value representing the user's expenses.

Responses
Success Response:
   When the data is submitted successfully, the server responds with a status   code 201 Created and a message indicating the success.
   Example: { "message": "Data submitted successfully" }

Error Responses:
   If the input data is not valid (e.g., non-numeric values or numbers exceeding a certain length), the server responds with a status code 400 Bad Request and an appropriate error message.
  Examples:
{ "error": "Invalid input. Please enter numeric values for income and expenses" }
{ "error": "Income and expenses must not exceed 10 digits" }


--Success Page--
URL: /success
Method: GET
This endpoint displays a success message to the user, indicating that their data was submitted correctly.

Responses
Success Response:
The server responds with a status code 200 OK and displays an HTML page with a success message.
Content: HTML page with success message.


Error Page
URL: /error
Method: GET
This endpoint displays an error message to the user, indicating that there was an issue with their data submission.

Request:
Query Params:
message: A string parameter that contains the specific error message to be displayed to the user.

Responses
Error Response:
The server responds with a status code 200 OK and displays an HTML page with the provided error message.
Content: HTML page with error message.


-----------Routes----------

--Home Route:--

Endpoint: /
Method: GET
Function: home()
Renders the homepage of the application.

--Submit Route:--

Endpoint: /submit
Method: POST
Function: submit()
Handles the submission of tax information. It performs server-side validation to ensure the data is numeric and within acceptable limits. If the data is valid, it is saved to the database, and a request is made to the OpenAI API to get tax advice. The user is then redirected to the success page with the tax advice.
Success Route:

Endpoint: /success
Method: GET
Function: success()
Displays the success page with the tax advice provided by the OpenAI API.


--Error Route:--

Endpoint: /error
Method: GET
Function: error()
Displays an error page with a specific error message passed as a query parameter.


# TASK 3
--------------Explanation of how the AI model is integrated---------------

---Setup Instructions---



--Prerequisites--

Python 3.x

Flask

SQLAlchemy

OpenAI Python client library



--AI Integration--

--Steps--


1st method :

1. Create a config.py file in the root directory of my project and add the  provided OpenAI API key:
  
  OPENAI_API_KEY = openai_api_key


2.Import necessary modules in app.py for the intergration of AI:  
  from sqlalchemy import create_engine
  from sqlalchemy.orm import sessionmaker
  from database_setup import Base, TaxInfo
  import openai
  import config

2.Initialize Flask app and database connection:
  app = Flask(__name_)
  engine = create_engine('sqlite:///tax_info.db')
  Base.metadata.bind = engine
  DBSession = sessionmaker(bind=engine)
  session = DBSession()

3.Set OpenAI API key: 
  openai.api_key = config.OPENAI_API_KEY

4.Define route to handle form submission and generate AI advice:
   The route sends a request to the OpenAI API (if the input data are correct/if validation is successful), including the user’s financial data. It prompts the AI to generate personalized tax advice based on the provided income and expenses.
   The AI-generated advice is extracted from the API response and cleaned up if necessary.
   
5.Render AI advice in success.html to redirect the user to the success page where the AI-generated tax advice is displayed.





2nd method : (Updated method to address GitHub violations)
To address GitHub violations due to the presence of sensitive information (OpenAI API key) in the code, the following steps were taken:

1. Create an .env in the root directory of my project and add the provided OpenAI API key:
  OPENAI_API_KEY = openai_api_key

2. Create a .gitignore file in the root directory of my project and add the .env

3. Updated the app.py file :
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

4. Push changes to GitHub repository


# TASK 4
-----------------------Containerization with Docker----------------------


--Steps--
 Step 1: Create Dockerfile
 Open project directory in VS Code and create a new file named Dockerfile with no   extension and a new .txt file named requirements.txt

 Step 2: Open Docker Desktop
 Download and install Docker Desktop from Docker's official website,
 Launch it and wait to start.

 Step 3: Build the Docker Image
 Open a terminal in VSCode, navigate to project directory and using this command : "docker build -t tax_filing_assistant ." This command tells Docker to build an image named tax_filing_assistant using the Dockerfile in the current directory (.).


 Step 4: Run the Docker Container
 Run the Docker container using this command "docker run -p 5000:5000 -e OPENAI_API_KEY=openai_api_key tax_filing_assistant" which contains:
-p 5000:5000: Maps port 5000 on your local machine to port 5000 in the container.
-e OPENAI_API_KEY=openai_api_key: Sets the OPENAI_API_KEY environment variable inside the container.
-tax_filing_assistant: The name of the Docker image to run.


 Step 5: Access the application at http://localhost:5000/.


# TASK 5
-----------------------DevOps and Continuous Integration----------------------

----Setting up the CI Pipeline---
--Steps--
 Step 1: Add Secrets to GitHub Repository for Docker username, Docker password and OpenAI API key. 
 
 Step 2: Create the CI Workflow File that contains these actions:
   -Name and Trigger the Pipeline
   -Defines the build job to run and specifies the runner environment, here it uses the latest Ubuntu version.
   -Lists the steps to execute in the job and uses the actions/checkout@v3 action to clone the repository.
   -Set up Python: Uses the actions/setup-python@v4 action to set up Python 3.10.
   -Install dependencies: Creates a virtual environment,activates it and installs the dependencies listed in requirements.txt.  
   -Run tests
   -Set up Docker Buildx: Uses the docker/setup-buildx-action@v2 action to set up Docker Buildx.
   -Builds a Docker image tagged tax_filing_assistant.
   -Defines the deploy job to run and specifies the runner environment, here it uses the latest Ubuntu version.
    -Lists the steps to execute in the job and uses actions/checkout@v3 action to clone the repository.
    -Uses the docker/setup-buildx-action@v2 action to set up Docker Buildx.
    -Logs into Docker Hub using secrets DOCKER_USERNAME and DOCKER_PASSWORD.
    -Builds and tags the Docker image with the username from the secrets.
    -Pushes the Docker image to Docker Hub.

 Step 3: Commit and Push Changes with following commands:
 git add .github/workflows/ci.yml
 git commit -m "Add CI pipeline with GitHub Actions"
 git push origin main

 Step 4: Monitor the CI Pipeline:
 Go to the "Actions" tab in my GitHub repository to monitor the CI pipeline. There I  can see the status of the build and deploy jobs.
