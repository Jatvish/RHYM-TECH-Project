from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS from flask_cors
import sqlite3

app = Flask(__name__)
CORS(app)  # Enable CORS for all endpoints

# Your database query function
def query_db(query, args=(), one=False):
    con = sqlite3.connect('RHYM(database).db')
    cur = con.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    con.close()
    return (rv[0] if rv else None) if one else rv

# Example endpoints for specific tables

# Malpedia endpoints
@app.route('/threat_actors1', methods=['GET'])
def get_threat_actors1():
    result = query_db('SELECT * FROM malpedia_ThreatActors1')
    return jsonify(result)

@app.route('/threat_actors2', methods=['GET'])
def get_threat_actors2():
    result = query_db('SELECT * FROM malpedia_ThreatActors2')
    return jsonify(result)

@app.route('/malware', methods=['GET'])
def get_malware():
    result = query_db('SELECT * FROM malpedia_malware')
    return jsonify(result)

# MITRE endpoints
@app.route('/techniques_enterprise', methods=['GET'])
def get_techniques_enterprise():
    result = query_db('SELECT * FROM mitre_TechniquesEnterprise')
    return jsonify(result)

@app.route('/techniques_ics', methods=['GET'])
def get_techniques_ics():
    result = query_db('SELECT * FROM mitre_TechniquesICS')
    return jsonify(result)

@app.route('/techniques_mobile', methods=['GET'])
def get_techniques_mobile():
    result = query_db('SELECT * FROM mitre_TechniquesMobile')
    return jsonify(result)

@app.route('/mitre_threat_actors', methods=['GET'])
def get_mitre_threat_actors():
    result = query_db('SELECT * FROM mitre_ThreatActors')
    return jsonify(result)

@app.route('/mitre_malware', methods=['GET'])
def get_mitre_malware():
    result = query_db('SELECT * FROM mitre_malware')
    return jsonify(result)

# Endpoint to list all available endpoints
@app.route('/', methods=['GET'])
def list_endpoints():
    endpoints = {
        'threat_actors1': 'http://127.0.0.1:5000/threat_actors1',
        'threat_actors2': 'http://127.0.0.1:5000/threat_actors2',
        'malware': 'http://127.0.0.1:5000/malware',
        'techniques_enterprise': 'http://127.0.0.1:5000/techniques_enterprise',
        'techniques_ics': 'http://127.0.0.1:5000/techniques_ics',
        'techniques_mobile': 'http://127.0.0.1:5000/techniques_mobile',
        'mitre_threat_actors': 'http://127.0.0.1:5000/mitre_threat_actors',
        'mitre_malware': 'http://127.0.0.1:5000/mitre_malware'
        # Add more endpoints here as needed
    }
    return jsonify(endpoints)

if __name__ == '__main__':
    print("Starting Flask app")
    app.run(debug=True)
