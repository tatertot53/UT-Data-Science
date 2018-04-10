import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite",echo=False)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Station = Base.classes.stations
Measurement = Base.classes.measurements

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################





app = Flask(__name__)


@app.route("/")
def home():
	print("Server received request for 'Home' page...")
	return (
		f"Welcome to my Homework 11 Homepage...<br/>"
		f"Available Routes:<br/>"
		f"/api/v1.0/precipitation<br/>"
		f"/api/v1.0/stations<br/>"
		f"/api/v1.0/tobs<br/><br/>"
		f"/api/v1.0/<start><br/>"
		f"(enter start date in 'YYYY-mm-dd' format at end of URL to view temp stats from that date to present)<br/>"
		f"EX: 'http://127.0.0.1:5000/2014-09-01'<br/><br/>"
		f"/api/v1.0/<start>/<end><br/>"
		f"(enter start date first, end date second in 'YYYY-mm-dd' format to view temp stats between those dates)<br/>"
		f"EX: 'http://127.0.0.1:5000/2012-04-05/2016-12-22'"
		)

@app.route("/api/v1.0/precipitation")
def precipitation():
	results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= '2016-08-23').all()
	date_temp_info = []
	for measurement in results:
		date_temp_dict = {
						'date' : measurement.date,
						'tobs' : measurement.tobs
		}
		date_temp_dict["date"] = measurement.date
		date_temp_dict["tobs"] = measurement.tobs
		date_temp_info.append(date_temp_dict)
	return jsonify(date_temp_info)

@app.route("/api/v1.0/stations")
def stations():
	results = session.query(Station.station,Station.name).all()
	station_info = []
	for station in results:
		station_name = {
						'station' : station.station,
						'name' : station.name
		}
		station_name["station"] = station.station
		station_name["name"] = station.name
		station_info.append(station_name)
	return jsonify(station_info)

@app.route("/api/v1.0/tobs")
def tobs():
    
    results = session.query(Measurement.date, Measurement.tobs).\
    				filter(Measurement.date.between(start_date, end_date)).\
                    order_by(Measurement.date).all()

    tobs_data = []
    for observations in results:
        tobs_dict = {
        			'date' : observations.date,
        			'tobs' : observations.tobs
        }
        tobs_dict["date"] = observations.date
        tobs_dict["tobs"] = observations.tobs
        tobs_data.append(tobs_dict)
    return jsonify(tobs_data)  

@app.route("/api/v1.0/<start_date>")
def temp_start(start_date):
	results = session.query(Measurement.date, func.min(Measurement.tobs).label('min_temp'), 
					func.avg(Measurement.tobs).label('avg_temp'), 
					func.max(Measurement.tobs).label('max_temp')).\
							filter(Measurement.date >= start_date).all()
	start_stats = []
	for stats in results:
		start_dict = {
					'min_temp' : stats.min_temp,
					'avg_temp' : stats.avg_temp,
					'max_temp' : stats.max_temp
		}
		start_dict["min_temp"] = stats.min_temp
		start_dict["avg_temp"] = stats.avg_temp
		start_dict["max_temp"] = stats.max_temp
		start_stats.append(start_dict)
	return jsonify(start_stats)

@app.route("/api/v1.0/<start_date>/<end_date>")
def temp_range(start_date, end_date):
	results = session.query(Measurement.date, func.min(Measurement.tobs).label('min_temp'), 
					func.avg(Measurement.tobs).label('avg_temp'), 
					func.max(Measurement.tobs).label('max_temp')).\
							filter((Measurement.date >= start_date) & (Measurement.date <= end_date)).all()
	range_stats = []
	for stats in results:
		range_dict = {
					'min_temp' : stats.min_temp,
					'avg_temp' : stats.avg_temp,
					'max_temp' : stats.max_temp
		}
		range_dict["min_temp"] = stats.min_temp
		range_dict["avg_temp"] = stats.avg_temp
		range_dict["max_temp"] = stats.max_temp
		range_stats.append(range_dict)
	return jsonify(range_stats)

if __name__ == "__main__":
    app.run(debug=True)
