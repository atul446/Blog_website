This website was built on my local computer using Django Framework,it can also be hosted on pythonanywhere.com 
Following are the steps to run this Website on a local computer:
1. Installing Python and Check the version
Download and Install Python: https://www.python.org/downloads/
Check Version from Command prompt
python --version
pip --version

2. Install Django globally
pip install Django
Check Version from cmd: Django-admin --version

3. Install Virtual Environment
pip install virtualenv
Check: pip list

4. Create Virtual Environment & Activate
py -m venv testenv  
Activate: testenv\Scripts\activate

5. Install Django for the project in venv(virtual environment)
pip install Django

6. Create a Django project
Django-admin start project demo app (demo app: project name)
Folder Structure:

Manage.py: helps us to run the command line to start server/project

7. create an app in the project folder (Single project can have multiple apps)
cd demo app
Create app:  python manage.py start app blog (blog: app name)

8. Run Project
manage.py runserver

Django-admin start project demo
cd demo
manage.py run server

