from flask import Flask, render_template, url_for
# Import Database table from data models e.g. Verb
from data.models import db, Verb
from flask_sqlalchemy import inspect

app = Flask(__name__)

# Call this function on any page before any database queries
def createDatabase():
    db.init_app(app)
    db.create_all()

# Call this method to convert database type to dictionary
def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
        for c in inspect(obj).mapper.column_attrs}

@app.route("/")
def index():
    createDatabase()
    return render_template("home.html")

# route = URL structure e.g. localhost:5000/verbs
@app.route("/verbs")
def verbs():
    createDatabase()
    
    # Create word in verb table
    verb1 = Verb('Aller')
    db.session.add(verb1)
    db.session.commit()
    
    # Query database for words in Verb table
    query = Verb.query.all()

    # Add verbs in database to list
    verbs = []
    for row in query:
        verb_dictionary = object_as_dict(row)
        for i in verb_dictionary:
            verbs.append(verb_dictionary[i])
    # Present list of verbs on the page
    return str(verbs)

@app.route("/adjectives")
def adjectives():
    createDatabase()
    return "Place adjectives here"

# Python magic - Runs the application
if __name__ == "__main__":
    app.run()
