# Creating a module. A module name must be in lowercase.
from flask import Flask, render_template

# Creating a variable of class Flask(OOP).
app=Flask(__name__)

# Creating a python decorator to route the homepage.
@app.route("/")
def main_jovian():
  return render_template('home.html')

if __name__=='__main__':
  # Access .run command by writing it as it was unaccessible.
  app.run(host="0.0.0.0", debug=True)
  # Host="0.0.0.0" means that the program will run on local host(the pc being used)
  # debug=True means that it will keep on debugging itself
  
  