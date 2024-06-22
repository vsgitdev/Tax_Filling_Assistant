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

 
