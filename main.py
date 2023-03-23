# Creating a module. A module name must be in lowercase.
from flask import Flask, render_template, jsonify
# jobs Variable to store data about jobs instead of using Database(as of now)
JOBS = [
   {
     "id" : "1",
     "title" : "Data Scientist",
     "location" : "Lahore, Pakistan",
     "salary" : "120,000"
   },
   {
    "id" : "2",
     "title" : "Database Manager",
     "location" : "Multan, Pakistan",
     "salary" : "100,000"
   },
   {
    "id" : "3",
     "title" : "Data Entry",
     "location" : "Karachi, Pakistan",
     "salary" : "$7,000"
   },
  {
    "id" : "3",
     "title" : "Data Entry",
     "location" : "Karachi, Pakistan",
     
   }
      ]
# Creating a variable of class Flask(OOP).
app=Flask(__name__)

# Creating a python decorator to route the homepage.
@app.route("/")
def main_jovian():
  return render_template('home.html', jobs=JOBS)

@app.route("/jobs")
def jobs_Jsonify():
  return jsonify(JOBS)

if __name__=='__main__':
  # Access .run command by writing it as it was unaccessible.
  app.run(host="0.0.0.0", debug=True)
  # Host="0.0.0.0" means that the program will run on local host(the pc being used)
  # debug=True means that it will keep on debugging itself
  
  