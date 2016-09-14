## @package flask.sh
# This is a short script written to verify that the dependencies of our project are present.
# Our project makes use of virtualenv, python, Flask, and several Flask extensions.  This script
# assumes that python and virtualenv are installed and in the system path.  You may omit the commands
# to activate and deactivate the virtual environment if you prepend '#!flask/bin/python' to the
# run.py script.
#
# Instructions
#
# 1. clone our project source into a git directory and navigate into the root
# 2. Run 'chmod +x flash.sh' from the command line to allow this script to execute
# 3. Run this script './flask.sh'
# 4. If all is well, your environment is ready
# 5. Start your virtual environment by typing 'source flask/bin/activate'
# 6. Stop your virtual environment by typing 'deactivate'
#
# Created by Stephen Longofono
# Adapted from a 2012 Flask tutorial written by Miguel Grinberg
# Accessed September 2016
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world/
#

#!/bin/bash
clear

echo " [ checking virtualenv version... ] "
# Virtualenv allows a virtual python environment to be created, in which you can run scripts
# and install packages in isolation from the rest of the system.  We need it because KU IT
# is rightfully restrictive about what packages we are allowed to install on the Linux machines (none).
# Specifically, the wtforms extension is not included, so we create a virtual environment and install
# whatever we please.
virtualenv --version
if [ $? -ne 0 ] ; then echo "Failed to verify virtualenv, check that it is installed and in your system path"; exit; fi

# Create a virtual environment for python in a folder named 'flask'
echo " [ creating virtual environment... ] "

virtualenv flask
# Alternately, comment out immediately above and uncomment below
#python -m venv flask

if [ $? -ne 0 ] ; then echo "Failed to create virtual environment, check that it and python are installed and in your system path"; exit; fi

# Download and install the extensions we need with the pip python installer
echo " [ setting up Flask... ] "
flask/bin/pip install flask
if [ $? -ne 0 ] ; then echo "Failed to download and install flask"; exit; fi
flask/bin/pip install flask-login
if [ $? -ne 0 ] ; then echo "Failed to download and install flask-login"; exit; fi
flask/bin/pip install flask-wtf
if [ $? -ne 0 ] ; then echo "Failed to download and install flask-wtf"; exit; fi

echo
echo " [ Success ] "
echo
