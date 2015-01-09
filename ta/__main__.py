from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import requests

app = Flask('taco_azimuth')

key = open('key.txt', 'r').read().strip()
print key

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/tacos', methods=['POST'])
def tacos():
    lat = float(request.form['lat'])
    lon = float(request.form['lon'])
    params = {
            'key': key,
            'location': '%f,%f' % (lat, lon),
            'rankby': 'distance',
            'opennow': True,
            'keyword': 'tacos'
            }
    etc = '&'.join( '%s=%s' % (k, params[k]) for k in params )
    r = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?%s' % etc)
    j = r.json()
    first_result = j['results'][0]['geometry']['location']
    target_lat = first_result['lat']
    target_lon = first_result['lng']
    print target_lat, target_lon
    return jsonify( {'lat':target_lat, 'lon':target_lon} )

app.debug = False
app.run(host='0.0.0.0')

