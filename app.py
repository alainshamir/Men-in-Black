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

if __name__ == "__main__":
    app.run(debug=True)
