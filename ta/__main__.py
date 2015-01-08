from flask import Flask
from flask import render_template

app = Flask('taco_azimuth')

key = open('key.txt', 'r').read().strip()
print key

@app.route('/')
def root():
    return render_template('index.html')

app.debug = False
app.run(host='0.0.0.0')

