# BookInfo
a Web App that provides information about random books.

## How to Use:

1. Clone the repo
2. Install Python and Pip
3. Open BookInfo folder through your terminal.
4. Install virtualenv
```
pip install virtualenv
```

4. Create a virtual environment in your project folder.
```
  virtualenv env
```
5. Activate the virual environment

  for windows:
```
  env/scripts/Activate.bat
```
  for mac:
```
  source env/bin/activate
```

4. Install python packages specified in requirements.txt
```
  pip install -r requirements.txt
```
5. run (change "py" to your relevant python interpreter if needed, i.e python3, python, etc..)
```
py app.py
```

or, if that didn't work:

for windows
```
  set Flask_APP=app.py
  flask run
```
  for mac
```
  export FLASK_APP=app.py
  flask run
```

6. enter this url in your web browser:
```
localhost:5000
```

