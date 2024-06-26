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

2.Initialize Git in the project directory running the following command:
  git init

3.Add all files to the repository running the following command:
  git add .

4.Commit the changes running the following command:
  git commit -m "Initial commit"

5.Push local repository to GitHub:
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

 5. Install the required packages: With the virtual environment activated, install all necessary dependencies listed in the `requirements.txt` file using the following command:
     pip install -r requirements.txt
   
 6. Run the Flask application using the following command:
        python app.py     

 7. Open your web browser and go to:
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

3. Create db_connection.py file, which manages database connection and session creation using SQLAlchemy.
  Specifically:
  Imports: Imports necessary SQLAlchemy modules (create_engine, sessionmaker, declarative_base).
 Base Definition: Defines Base using declarative_base(), which is used for defining SQLAlchemy models.
 Functions:
 get_engine: Returns a SQLAlchemy engine object configured with the specified    database URL (sqlite:///tax_info.db by default).
 get_session: Returns a SQLAlchemy session object bound to the provided engine (get_engine()).
 Initialization: Immediately initializes engine and session using get_engine() and get_session() respectively.

4. Create database_setup.py file which contains script that defines the database schema and the table structure. 
 defines the database schema and creates necessary tables.

 Imports: Imports necessary SQLAlchemy modules (Column, Integer, Float, Base) and the get_engine function from db_connection.py.
 Model Definition: Defines a SQLAlchemy model (TaxInfo) for the tax_info table with columns (id, income, expenses).
 Table Creation: Uses Base.metadata.create_all(engine) to create the database tables defined by the models in the specified engine (get_engine()).

4. Run database_setup.py to create the database and this will create tax_info.db with the defined table structure using this command :
   python database_setup.py


---------API Endpoints & Error handling----------

-Home Page


1. URL: /
Method: GET
Displays the home page with a form for users to submit their income and expenses.


2. URL: /submit
Method: POST
This endpoint accepts tax information from the user, specifically their income and expenses. The data is validated to ensure it is numeric and within acceptable limits.

Request Data Parameters: income & expenses.

Responses:

Success Response:
Status Code: 302 Found (Redirection to success page)
Redirects to the success page with AI-generated tax advice.

Error Responses:
Status Code: 302 Found (Redirection to error page)
Redirects to the error page with an appropriate error message.

(Best practice is to return the proper http rest api error code here for bad user input 400 Bad Request, but I couldn't succeed the automatic redirection to error page to inform the user.)


- Success Page

3. URL: /success

Method: GET

Displays a success message to the user, indicating that their data was submitted correctly and shows the AI-generated tax advice.

Responses:

Success Response:
Status Code: 200 OK
HTML page with a success message and tax advice.


-Error Page

4. URL: /error

Method: GET

Displays an error message to the user, indicating that there was an issue with their data submission.

Request Query Parameters: message: A string parameter that contains the specific error message to be displayed to the user.

Responses:
Error Response:
Status Code: 200 OK
HTML page with the provided error message.


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





2nd method : (Updated method to address GitHub violations and enhance security of the sensitive Apikey)
To address GitHub violations due to the presence of sensitive information (OpenAI API key) in the code, the following steps were taken:

1. Create an .env in the root directory of my project and add the provided OpenAI API key:
  OPENAI_API_KEY = openai_api_key

2. Create a .gitignore file in the root directory of my project and add the .env

3. Updated the app.py file :
openai.api_key = os.getenv('OPENAI_API_KEY')

4. Push changes to GitHub repository



# TASK 4
-----------------------Containerization with Docker----------------------


--Steps--
 1. Create Dockerfile
 Open project directory in VS Code and create a new file named Dockerfile with no   extension and a new .txt file named requirements.txt with all the required packages.

 2. Open Docker Desktop
 Download and install Docker Desktop from Docker's official website,
 Launch it and wait to start.

 3. Build the Docker Image
 Open a terminal in VSCode, navigate to project directory and using this command : "docker build -t tax_filing_assistant ." This command tells Docker to build an image named tax_filing_assistant using the Dockerfile in the current directory (.).


 4. Run the Docker Container
 Run the Docker container using this command:
 "docker run -p 5000:5000 -e OPENAI_API_KEY=openai_api_key tax_filing_assistant" which contains:
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

 3. Commit and Push Changes with following commands:
 git add .github/workflows/ci.yml
 git commit -m "Add CI pipeline with GitHub Actions"
 git push origin main

 4. Monitor the CI Pipeline:
 Go to the "Actions" tab in my GitHub repository to monitor the CI pipeline. There I  can see the status of the build and deploy jobs.
