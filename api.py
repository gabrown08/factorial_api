import flask
import json
from flask_api import FlaskAPI
from flask import request, jsonify

# create app object
app = FlaskAPI(__name__)
app.config['DEBUG'] = True

# open save file
with open('factorial_dict.json', 'r+') as f:
    data = json.loads(f.read())

# sorts the database keys numerically
def numericalSort(data):
    data2 = {}
    new_keys = []
    for i in list(data.keys()):
        new_keys.append(int(i))
    for j in sorted(new_keys):
        data2[str(j)] = data[str(j)]
    return data2

# recursive factorial
def factorial(n):
  if n == 1:
    return n
  else:
    return(n*factorial(n-1))

# homepage
@app.route('/', methods=['GET'])
def home():
    home = {}
    home["/"] = 'homepage'
    home["/database"] = 'display n! database'
    home["/factorial/n"] = 'add n! to factorial database'
    return home

# displays
@app.route('/database', methods=['GET'])
def factorial_database():
    return numericalSort(data)

# adds n! to database
@app.route('/factorial/<int:n>', methods=['GET'])
def n_factorial(n):
    try:
        type(data[str(n)])
    except KeyError:
        data[str(n)] = factorial(n)
        with open('factorial_dict.json', 'w') as f:
            f.write(str(json.dumps(numericalSort(data), indent=2)))
    return {f"{n}": f"{data[str(n)]}"}

# run app
app.run()
