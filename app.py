<<<<<<< HEAD
import os
import json
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

import sqlite3 as sql

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db/date_a_park.sqlite"
# db = SQLAlchemy(app)

# from .models import *


# Create a route that renders MenInBlack.html template
@app.route("/")
def home():
    return render_template("MenInBlack.html")

@app.route("/Homicides")
def Homicides():
    """ Get all the offenses """
    db_path = os.path.join('static','data','dc_crime.sqlite')
    con = sql.connect(db_path)
    cursor = con.cursor()
    cursor.execute("SELECT Offense, Year, COUNT(*) As 'num' FROM crime GROUP BY Offense,Year")
    data = jsonify(cursor.fetchall())

    con.close()
    
    print(data)

    return data
# print(offenses)

@app.route("/Robbery")
def robbery():
    """ Get all the robbery """
    db_path = os.path.join('static','data','dc_crime.sqlite')
    con = sql.connect(db_path)
    cursor = con.cursor()
    cursor.execute("SELECT Offense, Year, COUNT(*) As 'num' FROM crime WHERE(Offense='robbery') GROUP BY Offense,Year")
    data = jsonify(cursor.fetchall())

    con.close()
    
    print(data)

    return data
# print(Robbery)

@app.route("/cluster 1")
def cluster_1():
    """ Get all the robbery """
    db_path = os.path.join('static','data','dc_crime.sqlite')
    con = sql.connect(db_path)
    cursor = con.cursor()
    cursor.execute("SELECT Offense, Year, COUNT(*) As 'num' FROM crime WHERE(Neighborhood='cluster 1') and Offense in ('homicide') GROUP BY Offense,Year")
    data = jsonify(cursor.fetchall())

    con.close()
    
    print(data)

    return data
# print(cluster 1)

@app.route("/motor vehicle theft")
def motor_vehicle_theft():
    """ Get all the motor vehicle theft """
    db_path = os.path.join('static','data','dc_crime.sqlite')
    con = sql.connect(db_path)
    cursor = con.cursor()
    cursor.execute("SELECT Offense, Year, COUNT(*) As 'num' FROM crime WHERE(Offense='motor vehicle theft') GROUP BY Offense,Year")
    data = jsonify(cursor.fetchall())

    con.close()
    
    print(data)

    return data
print(motor_vehicle_theft)

@app.route("/cluster 2")
def cluster_2():
    """ Get all the motor vehicle theft """
    db_path = os.path.join('static','data','dc_crime.sqlite')
    con = sql.connect(db_path)
    cursor = con.cursor()
    cursor.execute("SELECT Offense, Year, COUNT(*) As 'num' FROM crime WHERE(Neighborhood='cluster 2') and Offense in ('homicide') GROUP BY Offense,Year")
    data = jsonify(cursor.fetchall())

    con.close()
    
    print(data)

    return data
# print(cluster 2)

@app.route("/theft_other")
def theft_other():
    """ Get all the theft/other """
    db_path = os.path.join('static','data','dc_crime.sqlite')
    con = sql.connect(db_path)
    cursor = con.cursor()
    cursor.execute("SELECT Offense, Year, COUNT(*) As 'num' FROM crime WHERE(Offense='theft/other') GROUP BY Offense,Year")
    data = jsonify(cursor.fetchall())

    con.close()
    
    print(data)

    return data
# print(theft_other)

@app.route("/cluster 3")
def cluster_3():
    """ Get all the theft/other """
    db_path = os.path.join('static','data','dc_crime.sqlite')
    con = sql.connect(db_path)
    cursor = con.cursor()
    cursor.execute("SELECT Offense, Year, COUNT(*) As 'num' FROM crime WHERE(Neighborhood='cluster 3') and Offense in ('homicide') GROUP BY Offense,Year")
    data = jsonify(cursor.fetchall())

    con.close()
    
    print(data)

    return data
# print(cluster 3)


@app.route("/assault_with_dangerous_weapon")
def assault_with_dangerous_weapon():
    """ Get all the assault_with_dangerous_weapon """
    db_path = os.path.join('static','data','dc_crime.sqlite')
    con = sql.connect(db_path)
    cursor = con.cursor()
    cursor.execute("SELECT Offense, Year, COUNT(*) As 'num' FROM crime WHERE(Offense='assault w/dangerous weapon') GROUP BY Offense,Year")
    data = jsonify(cursor.fetchall())

    con.close()
    
    print(data)

    return data
# print(assault_with_dangerous_weapon)

@app.route("/cluster 4")
def cluster_4():
    """ Get all the assault_with_dangerous_weapon """
    db_path = os.path.join('static','data','dc_crime.sqlite')
    con = sql.connect(db_path)
    cursor = con.cursor()
    cursor.execute("SELECT Offense, Year, COUNT(*) As 'num' FROM crime WHERE(Neighborhood='cluster 4') and Offense in ('homicide') GROUP BY Offense,Year")
    data = jsonify(cursor.fetchall())

    con.close()
    
    print(data)

    return data
# print(assault_with_dangerous_weapon)


@app.route("/sex_abuse")
def sex_abuse():
    """ Get all the sex_abuse """
    db_path = os.path.join('static','data','dc_crime.sqlite')
    con = sql.connect(db_path)
    cursor = con.cursor()
    cursor.execute("SELECT Offense, Year, COUNT(*) As 'num' FROM crime WHERE(Offense='sex abuse') GROUP BY Offense,Year")
    data = jsonify(cursor.fetchall())

    con.close()
    
    print(data)

    return data
# print(sex_abuse)

@app.route("/cluster 5")
def cluster_5():
    """ Get all the sex_abuse """
    db_path = os.path.join('static','data','dc_crime.sqlite')
    con = sql.connect(db_path)
    cursor = con.cursor()
    cursor.execute("SELECT Offense, Year, COUNT(*) As 'num' FROM crime WHERE(Neighborhood='cluster 5') and Offense in ('homicide') GROUP BY Offense,Year")
    data = jsonify(cursor.fetchall())

    con.close()
    
    print(data)

    return data
# print(sex_abuse)

@app.route("/cluster 6")
def cluster_6():
    """ Get all the sex_abuse """
    db_path = os.path.join('static','data','dc_crime.sqlite')
    con = sql.connect(db_path)
    cursor = con.cursor()
    cursor.execute("SELECT Offense, Year, COUNT(*) As 'num' FROM crime WHERE(Neighborhood='cluster 6') and Offense in ('homicide') GROUP BY Offense, Year")
    data = jsonify(cursor.fetchall())

    con.close()
    
    print(data)

    return data

@app.route("/cluster 7")
def cluster_7():
    """ Get all the sex_abuse """
    db_path = os.path.join('static','data','dc_crime.sqlite')
    con = sql.connect(db_path)
    cursor = con.cursor()
    cursor.execute("SELECT Offense, Year, COUNT(*) As 'num' FROM crime WHERE(Neighborhood='cluster 7') and Offense in ('homicide') GROUP BY Offense, Year")
    data = jsonify(cursor.fetchall())

    con.close()
    
    print(data)

    return data

@app.route("/cluster 8")
def cluster_8():
    """ Get all the sex_abuse """
    db_path = os.path.join('static','data','dc_crime.sqlite')
    con = sql.connect(db_path)
    cursor = con.cursor()
    cursor.execute("SELECT Offense, Year, COUNT(*) As 'num' FROM crime WHERE(Neighborhood='cluster 8') and Offense in ('homicide') GROUP BY Offense, Year")
    data = jsonify(cursor.fetchall())

    con.close()
    
    print(data)

    return data

@app.route("/cluster 9")
def cluster_9():
    """ Get all the sex_abuse """
    db_path = os.path.join('static','data','dc_crime.sqlite')
    con = sql.connect(db_path)
    cursor = con.cursor()
    cursor.execute("SELECT Offense, Year, COUNT(*) As 'num' FROM crime WHERE(Neighborhood='cluster 9') and Offense in ('homicide') GROUP BY Offense, Year")
    data = jsonify(cursor.fetchall())

    con.close()
    
    print(data)

    return data

@app.route("/cluster 21")
def cluster_21():
    """ Get all the sex_abuse """
    db_path = os.path.join('static','data','dc_crime.sqlite')
    con = sql.connect(db_path)
    cursor = con.cursor()
    cursor.execute("SELECT Offense, Year, COUNT(*) As 'num' FROM crime WHERE(Neighborhood='cluster 1') and Offense in ('homicide') GROUP BY Offense, Year")
    data = jsonify(cursor.fetchall())

    con.close()
    
    print(data)

    return data

@app.route("/cluster 37")
def cluster_37():
    """ Get all the sex_abuse """
    db_path = os.path.join('static','data','dc_crime.sqlite')
    con = sql.connect(db_path)
    cursor = con.cursor()
    cursor.execute("SELECT Offense, Year, COUNT(*) As 'num' FROM crime WHERE(Neighborhood='cluster 37') and Offense in ('homicide') GROUP BY Offense, Year")
    data = jsonify(cursor.fetchall())

    con.close()
    
    print(data)

    return data
# print(sex_abuse)

@app.route("/send", methods=["GET"])
def send():
    # need the names of things that are checked
    # loop through request.form (should be dictionary)
    # then get only the "checked" ones
    if request.method == "GET":
        print("Hello")
        print(request.args)
        form_data = request.args
        # get the offenses keys
        #offenses = []
        query = "SELECT DISTINCT crime.NEIGHBORHOOD, crime.METHOD, crime.offense FROM crime "
        #query += "INNER JOIN activities ON parks.ID = activities.ID "
        query += "WHERE (" # offenses.offensegroup = "
        for offense in form_data:
            query += "crime.offense = '" + offense + "' AND "

        # remove that last " AND " (5 characters)
        #query = query[:-5]
        #query += ");"

        #print(query)
        # Now we need the SQL query
        
        db_path = os.path.join('static','data','dc_crime.sqlite')
        con = sql.connect(db_path)
        con.text_factory = lambda x: str(x, 'utf-8')
        cursor = con.cursor()
        # # cursor.execute("select name from sqlite_master where type = 'table';")
        cursor.execute(query)
        data = cursor.fetchall()
        # names = list(map(lambda x: x[0], cursor.description))
        # print(names)

        

        return jsonify(data)
        # results = db.session.query(Parks.name, Parks.lat, Parks.lon).all()
        # #results = db.session.query(Parks.name, Parks.lat, Parks.lon).filter(Parks.id == '4')

        # name = [result[0] for result in results]
        # lat = [result[1] for result in results]
        # lon = [result[2] for result in results]

        # park_data = [{
        #     "type": "scattergeo",
        #     "locationmode": "USA-states",
        #     "name": name,
        #     "lat": lat,
        #     "lon": lon,
        #     "text": name,
        #     "hoverinfo": "text",
        #     "marker": {
        #         "size": 5,
        #         "line": {
        #             "color": "rgb(8,8,8)",
        #             "width": 1
        #         },
        #     }
        # }]

        # return jsonify(park_data)
    return # This is if the requeset is not a GET method

@app.route("/crime")
def crime():
    return jsonify(json.load(open(os.path.join('static', 'data', 'crime.geojson'))))
=======
# Import our pymongo library, which lets us connect our Flask app to our Mongo database.

import pymongo

from flask import Flask, render_template



# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://guy:shamir88@ds121593.mlab.com:21593/dc_crime_complete'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.dc_crime_complete

# Drops collection if available to remove duplicates
# db.team.drop()

# Creates a collection in the database and inserts two documents
# db.team.insert_many(
#     [
#         {
#             'player': 'Jessica',
#             'position': 'Point Guard'
#         },
#         {
#             'player': 'Mark',
#             'position': 'Center'
#         }
#     ]
# )


# Set route
@app.route('/')
def index():
    # Store the entire team collection in a list
    offensegroup = list(db.crime.find())
    print(offensegroup)

    # Return the template with the teams list passed in
    #return render_template('MenInBlack.html', offensegroup=offensegroup)
    return render_template('template.html', offensegroup=offensegroup)
>>>>>>> 809b5fe3d844cb49b2eeabf8228846c795fac9e2

if __name__ == "__main__":
    app.run(debug=True)
