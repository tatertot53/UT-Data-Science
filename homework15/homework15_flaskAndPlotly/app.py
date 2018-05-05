import json
from flask import (
    Flask,
    render_template,
    jsonify,
    request)


#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Database Setup
#################################################
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

import os
import pandas as pd 
import numpy as np 
import plotly

# The database URI
engine = create_engine('sqlite:///db/belly_button_biodiversity.sqlite', echo=False)
Base = automap_base()
Base.prepare(engine, reflect=True) 
session = Session(engine)

Metadata = Base.classes.samples_metadata
OTU = Base.classes.otu
Samples = Base.classes.samples

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/bellyButtons.sqlite"

db = SQLAlchemy(app)

# Base = automap_base()


def __repr__(self):
    return '<Bio %r>' % (self.name)



@app.before_first_request
def setup():
	db.drop_all()
	db.create_all()

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/otu")
def otu_descriptions():
	otu_descriptions = []
	for description in session.query(OTU.lowest_taxonomic_unit_found).all():
		otu_descriptions.append(description[0])
	return jsonify(otu_descriptions)

@app.route("/names")
def otus():
	otu_list = []
	for sample_id in session.query(Metadata.SAMPLEID).all():
		names = {}
		otu_list.append("BB_" + str(sample_id[0]))
	return jsonify(otu_list)

@app.route("/metadata")
@app.route("/metadata/<sample>")
def sample_info(sample):
	sample_id=int(sample)
	sel = [Metadata.SAMPLEID, Metadata.ETHNICITY,
           Metadata.GENDER, Metadata.AGE,
           Metadata.LOCATION, Metadata.BBTYPE]
	results = session.query(*sel).\
		filter(Metadata.SAMPLEID == sample).all()

	sample_metadata = {}
	for result in results:
		sample_metadata['AGE'] = result[0]
		sample_metadata['BBTYPE'] = result[1]
		sample_metadata['ETHNICITY'] = result[2]
		sample_metadata['GENDER'] = result[3]	
		sample_metadata['LOCATION'] = result[4]
		sample_metadata['SAMPLEID'] = result[5]
		
	return jsonify(sample_metadata)

@app.route("/wfreq")
@app.route("/wfreq/<sample>")
def washes(sample):
	results = session.query(Metadata.WFREQ).\
		filter(Metadata.SAMPLEID == sample).all()
	wfreq = np.ravel(results)

	return jsonify(int(wfreq[0]))

@app.route("/samples/<sample>") 
def RetunSampleData(sample):
    sort_values= session.query(Samples.otu_id,sample).order_by(sample+" desc").limit(100).all()
    result = [{"otu_id" : [c[0] for c in sort_values],
          "sample_values" : [c[1] for c in sort_values]}]
    return jsonify(result)

# @app.route('/samples/<sample>')
# def samples(sample):
# 	stmt = session.query(Samples).statement
# 		df = pd.read_sql_query(stmt, session.bind)

# 		# Make sure that the sample
# 		if sample not in df.columns:
# 			return jsonify(f"Error! Sample: {sample} Not Found!"), 400	
		
# 		# Return any sample values
# 		df = df[df[sample] > 1]
		
# 		# Sort the results by samples
# 		df.sort_values(by=sample, ascending=0)
		
# 		# Format the data to send as JSON
# 		data = [{
# 			"otu_ids": df[sample].index.values.tolist(),
# 			"sample_values": df[sample].values.tolist()
# 		}]
# 		return jsonify(data)



if __name__ == "__main__":
	app.run(debug=True)