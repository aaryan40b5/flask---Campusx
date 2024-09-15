from flask import Flask #from this flask library import Flask class
#when we write import statements, python actually executes those modules that we import

#now we will create an object of our application
ap = Flask(__name__)
# __name__ is a special variable which python assigns to each module(file)

#now we will create our first endpoint - Home Page

# / -> means our homepage
@ap.route("/") #decorator for creating an endpoint
@ap.route("/home") #for the same function we can have multiple routes
def home():
    return "<h1>Welcome to the Home Page!</h1>"
# whenever someone comes to / endpoint, this function will get called

@ap.route("/welcome/<name>") #we want a parameter from the user so , <name> is a parameter entered by the user
def welcome(name):
    return f"<h1>hi {name}, you're welcome to this page!</h1>"

#example on giving path parameter - 1 input
@ap.route("/addition/<int:num>") #int: ka matlab hai we are expecting an integer parameter. yeh nhi lagaoge toh flask num ko string maan lega
def addition(num):
    return f"<h1>input is {num}, output is {num+10}</h1>"

#example on giving path parameter - multiple inputs
@ap.route("/addition_three/<float:num1>/<float:num2>/<float:num3>")
def additon_3(num1,num2,num3):
    return f"{num1} + {num2} + {num3} = {num1+num2+num3}"  
  

@ap.route("/about")
def about():
    return "<h1>Welcome to the About Page!</h1>"

#start the application only if we are running this particular module
if __name__ == "__main__":
    ap.run(debug=True) # agar kuch errors aa rhe he ya kuch ho rha h toh "debug=True" hame logs dega


