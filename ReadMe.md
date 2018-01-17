

#To run the application if you are using Linux or OSX:

    Open the Linux Command Line 
    And Input the following commands
    
#Install python:

    sudo apt-get update

    sudo apt-get -y upgrade

    sudo apt-get install -y python3-pip


#Install virtualenv

    sudo pip install virtualenv
    
    fo Ubuntu try:
    
    sudo apt-get install python-virtualenv
    

#Install Environment
    mkdir myproject
    cd myproject
    virtualenv venv


#Install Flask
    sudo pip install Flask




#Run Application
    
    Head towards the Project Directory HomeTestCoding, if you 
    are not already in it, where you extracted it:
    
    cd ../HomeTestCoding/server/Routes
    
    then input:
    
    FLASK_APP=MainRoute.py

    FLASK_DEBUG=1

    run flask
    
    then open a browser and head towards http://127.0.0.1:5000/

#If you are using windows:

    Download python right here:https://www.python.org/ftp/python/3.6.3/python-3.6.3.exe    
    
    And follow the quick installation wizard
    
       
    
#pip and setuptools on Windows
    
    If you don't have pip install please run: get-pip.py
    it is located inside the HomeTestCoding  
    
    After it is done running, open Command Line as Administrator
    and input the following:
    
    pip install --upgrade pip setuptools
    
    pip install virtualenv
    
    
    
    
    
