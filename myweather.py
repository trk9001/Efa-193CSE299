from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myweather.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class WeatherInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    humidity = db.Column(db.String(50))
    pressure_hg = db.Column(db.String(50))
    pressure_mb = db.Column(db.String(50))
    rain = db.Column(db.String(50))
    temperature = db.Column(db.String(50))

    def __repr__(self):
        return '<WeatherInfo ({})>'.format(self.time)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/v1/today')
def today_weather():
    """Retrieve the current weather data and return it in JSON."""
    today = {
        'humidity': '0',
        'pressure_hg': '0',
        'pressure_mb': '0',
        'rain': '0',
        'temperature': '69',
    }
    return today
