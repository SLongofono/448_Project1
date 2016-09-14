# 448_Project1

Calendar project for software engineering, EECS448

Instructions:
  0. Install virtualenv and python on your machine, add to your system path
  1. Clone this repo into a local folder
  2. Change flask.sh to be executable (see comments within for detailed instructions)
  3. Run flask.sh to set up the virtual environment and the directory hierarchy
  4. Create config.py with your parameters in this format: 'PARAM=value'.
    Example contents of config.py:
        
        DEBUG=True
        SECRET_KEY='YourSecretKeyHere'
        USERNAME='YourUserNameHere'
        PASSWORD='YourPasswordHere'
        
  5. Move config.py to the same level as the 'app' directory
  6. Start the virtual environment: from within the flask folder, type 'source bin/activate'
  7. Start the server: from the directory which contains the 'app' folder, type './run.py'
  8. Open a browser and navigate to 'http://localhost:5000/'
  
