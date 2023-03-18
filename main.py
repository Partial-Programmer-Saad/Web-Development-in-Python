# Creating a module. A module name must be in lowercase.
from flask import Flask

# Creating a variable of class Flask(OOP).
app=Flask(__name__)

# Creating a python decorator to route the homepage.
@app.route("/")
def hello_world():
  return "Hello World"

if __name__=='__main__':
  # Access .run command by writing it as it was unaccessible.
  app.run(host="0.0.0.0", debug=True)