import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Database Setup
engine = create_engine("../Resources/sqlite:///hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Passenger = Base.classes.passenger

# Create our session (link) from Python to the DB
session = Session(engine)

# Flask Setup
app = Flask(__name__)

# Flask Routes

@app.route("/")
def home():
    """List all available API routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """List of Precipitation"""
    
@app.route("/api/v1.0/stations")
def stations():
    """List of Weather Stations"""
    
@app.route("/api/v1.0/<start>")
def vacationstartdate():
    """Vacation Start Date Information"""

@app.route("/api/v1.0/<start>/<end>")
def vacationstartandenddates():
    """Vacation Start Date and End Date Information"""

if __name__ == "__main__":
    app.run(debug=True)
