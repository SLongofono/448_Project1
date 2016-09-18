# 448_Project1

Our calendar project for software engineering, EECS448.  The goal was to create a
calendar application which allowed a single user to view years, months, weeks, and
days in an academic calendar year.  Individual days track persistent details which the
user can add or remove at will.

We were not permitted to use a database, so we used a logfile to fake one.  Some of
us wanted to explore Flask as a web framework, so we wrote a server and client to display
the application.

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
     
     At this point your local cloned git directory should look like this:

	     cloned_folder/
	        ->app/
                   ->static
                   ->templates
                   ->app files
	        ->flask/
	        ->config.py
	        ->flask.sh
	        ->LICENSE
	        ->README.md
	        ->run.py
     

  6. Start the virtual environment: from within the flask folder, type 'source bin/activate'
  7. Start the server: from the directory which contains the 'app' folder, type './run.py'
  8. Open a browser and navigate to 'http://localhost:5000/'.  Your username and password
     should match what you put in the config.py file.
