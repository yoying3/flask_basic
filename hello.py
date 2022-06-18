from flask import Flask,render_template


# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')
# def index():
#   return "<h1>Hello World</h1>"

# safe -> 在.py裡用<tag>，要在html的變數後面加｜safe 會使用<tag>的功能
# striptags -> 在.py裡用<tag>，要在html的變數後面加｜striptags 會自動忽略移除<tag>的作用
# lower  , upper , title ,  trim 移除大寫功能 

def index():
    first_name = "YoYing"
    stuff = "This is Bold text"
    favorite_pizza = ["Pepperoni","Cheese","Mushrooms",41]
    return render_template("index.html",
                           first_name=first_name,
                           stuff=stuff,
                           favorite_pizza=favorite_pizza)


@app.route('/user/<name>')

def user(name):
    return render_template("user.html",user_name=name)

# Creat Custom Error Pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404
# Invalid Server URL
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"),500
