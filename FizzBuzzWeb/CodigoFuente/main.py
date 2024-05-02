"""Main File of project by Sebastian Lopez"""
from flask import Flask, request
from my_app import MyApp

app = Flask(__name__)
my_app=MyApp()

@app.route('/numbers/<number>', methods=['GET','POST','DELETE'])
def numbers(number):
    """method to URL numbers"""
    if request.method == "GET":
        return my_app.get(int(number))
    if request.method == "POST":
        return my_app.post(int(number))
    if request.method == "DELETE":
        return my_app.delete(int(number))
    return "Not Allowed Method",400

@app.route('/range/', methods=["POST"])
def range_post():
    """method to range"""
    if request.method=="POST":
        limits = request.get_json()
        min_limit=limits["min_limit"]
        max_limit=limits["max_limit"]
        return my_app.range_post(int(min_limit),int(max_limit))
    return "Not Allowed Method",400
app.run(host='0.0.0.0', port=81)
