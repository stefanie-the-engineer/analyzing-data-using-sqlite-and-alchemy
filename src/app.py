import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Database Setup
engine = create_engine("sqlite:///../../Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect = True)

# Save reference to the table
Station = Base.classes.hawaii_stations
Measurement = Base.classes.hawaii_measurements

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
    # Query all precipitation data
    results = session.query(Measurement.prcp).all()

    # Convert list of tuples into normal list
    all_precipitations = list(np.ravel(results))

    return jsonify(all_precipitations)

    
@app.route("/api/v1.0/stations")
def stations():
    """List of Weather Stations"""
    # Query all weather station data
    results = session.query(Station.station).all()
    
    # Convert list of weather stations into normal list
    all_stations = list(np.ravel(results))
    
    return jsonify(all_stations)

@app.route("/api/v1.0/<start>")
def vacationstartdate(start):
    """Vacation Start Date Information"""
    # Query the weather data
    results = session.query(Measurement.prcp).all()
    
    # Convert list of precipitation lists into normal list
    one_day_precipitation = list(np.ravel(results))
    
    # Canonicalize the start date
    canonicalized = start.replace("-", "")
    
    if start == canonicalized:
        return jsonify(one_day_precipitation)

    return jsonify({"error": f"Weather for {start} not found."}), 404

@app.route("/api/v1.0/<start>/<end>")
def vacationstartandenddates(start, end):
    """Vacation Start Date and End Date Information"""
    # Query the weather data
    results = session.query(Measurement.prcp).all()
    
    # Convert list of precipitation lists into normal list
    trip_precipitation = list(np.ravel(results))
    
    # Canonicalize the start date
    canonicalized = start.replace("-", "")
    canonicalized = end.replace("-", "")
    
    if start == canonicalized and end == canonicalized:
        return jsonify(trip_precipitation)

    return jsonify({"error": f"Weather for {start} and {end} not found."}), 404

if __name__ == "__main__":
    app.run(debug=True)