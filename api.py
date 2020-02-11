import flask
import json
from flask_api import FlaskAPI
from flask import request, jsonify


# create app object
app = FlaskAPI(__name__)
app.config['DEBUG'] = True

# open save file
with open('api_dict.json', 'r+') as f:
    data = json.loads(f.read())

# recursive factorial
def factorial(n):
  # print(n)
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
    home["/factorial/n"] = 'adds n! to database'
    return home

# displays
@app.route('/database', methods=['GET'])
def database():
    return data

# adds n! to database
@app.route('/factorial/<int:n>', methods=['GET'])
def nfactorial(n):
    try:
        type(data[str(n)])
    except KeyError:
        data[str(n)] = factorial(n)
        with open('api_dict.json', 'w') as f:
            f.write(str(json.dumps(data, sort_keys=True, indent=2)))
    return {f"{n}": f"{data[str(n)]}"}

# run app
app.run()
