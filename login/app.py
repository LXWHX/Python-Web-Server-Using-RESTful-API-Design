from pprint import pprint
import pymongo
from dataclasses import dataclass
from flask import Flask
from flask import request, render_template, redirect, url_for, session, g
import json


app = Flask(__name__, static_url_path="/")
app.config['SECRET_KEY'] = "sdfklas0lk42j"

PORT = 5000
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["4564FinalProj"]
mycol = mydb["UserInfo"]
mycol2 = mydb["ButtonInfo"]

mylist = [
    {"_id": "1", "user": "Yuwei Wang", "password": "123", "age": "22", "gender": "Male", "potential illness": "Low Blood Pressure",
     "emergency_contact1": "danielpm@vt.edu", "emergency_contact2": "shiqianl18@vt.edu", "emergency_phone_call": "9083324782", "location": "bathroom"},
    {"_id": "2", "user": "Daniel Mauro", "password": "123", "age": "22", "gender": "Male", "potential illness": "High Blood Presure",
     "emergency_contact1": "yuweiwang@vt.edu", "emergency_contact2": "shiqianl18@vt.edu", "emergency_phone_call": "9083324782", "location": "bathroom"},
    {"_id": "3", "user": "Shiqian Li", "password": "123", "age": "22", "gender": "Female", "potential illness": "Low Blood Sugar",
     "emergency_contact_email1": "danielpm@vt.edu", "emergency_contact_email2": "yuweiwang@vt.edu", "emergency_phone_call": "9083324782", "location": "bathroom"}
]

# mycol.insert_many(mylist)


@dataclass
class User:
    id: str
    username: str
    password: str


users = []

for user in mycol.find({}):
    id = user["_id"]
    username = user["user"]
    password = user["password"]
    users.append(User(id, username, password))


@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        user = None
        for u in users:
            if u.id == session['user_id']:
                user = u
        g.user = user


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)
        username = request.form.get("username", None)
        password = request.form.get("password", None)

        user = mycol.find_one({"user": username})

        if user == None:
            return render_template("login.html")

        if user["password"] == password:
            session['user_id'] = user["_id"]
            mycol2.update_one({"button": "1"}, {
                "$set": {"curr_user": username}})
            mycol2.update_one({"button": "2"}, {
                "$set": {"curr_user": username}})
            print("User Updated")
            return redirect(url_for('profile'))

    return render_template("login.html")


@app.route("/profile")
def profile():
    if not g.user:
        return redirect(url_for('login'))

    return render_template("profile.html")


@app.route("/update", methods=['POST'])
def update():
    params = json.loads(request.get_json())
    id = params["_id"]
    print("Id:")
    print(id)
    mycol.update_one({"_id": id}, {
                     "$set": {"user": params["username"]}})
    mycol.update_one({"_id": id}, {
                     "$set": {"password": params["password"]}})
    mycol.update_one({"_id": id}, {"$set": {"age": params["age"]}})
    mycol.update_one({"_id": id}, {
                     "$set": {"gender": params["gender"]}})
    mycol.update_one({"_id": id}, {
                     "$set": {"potential illness": params["potentialIllness"]}})
    mycol.update_one({"_id": id}, {
                     "$set": {"emergency_contact1": params["ec1"]}})
    mycol.update_one({"_id": id}, {
                     "$set": {"emergency_cantact2": params["ec2"]}})
    mycol.update_one(
        {"_id": id}, {"$set": {"emergency_phone_call": params["epn"]}})
    mycol.update_one({"_id": id}, {
                     "$set": {"location": params["location"]}})

    users[id - 1] = User(id, params["username"], params["password"])

    return render_template("profile.html")


@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
