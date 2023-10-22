from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Web World!"

"""
1. create a folder 
eg: 'test FLASK rad'

2. open folder with code editor 
eg: 'VS code'

3. create Virtual Envirement from VSCODE terminal 
eg: -->python -m venv venv

4. activate venv from vscode terminal 
eg: -->venv\Scripts\activate

5. install Flask Framework 
eg: -->python -m pip install flask

6. create requirements.txt 
eg: -->pip freeze > requirements.txt

7. create a python file named app.py and start coding...

8. set app.py to flask envirements variables 
eg: -->set FLASK_APP=app.py

9. run flask server
eg: -->run flask

10. go to http://127.0.0.1:5000 in browser

11. Yay! Welcome to Web World...
"""