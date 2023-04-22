# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():
    name = "Laksh" # write your name
    age = "15" # write your age

    return render_template('index.html' , me_name = name , me_age = age)

# define the route to father webpage
@app.route("/home_2")
def home2():
    name2 ="Harish"
    age2 = "48"

    return render_template('father.html' , father_name = name2 , father_age = age2)

# define the route to mother webpage
@app.route("/home_3")
def home3():
    name3 = "Archana"
    age3 = "45"

    return render_template('mother.html' , mother_name = name3 , mother_age = age3)

# define the route to friends webpage
@app.route("/home_4")
def home4():
    name4 = "Himesh"
    age4 = "13"

    return render_template('friend.html' , friend_name = name4 , friend_age = age4)

# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
