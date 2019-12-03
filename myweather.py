import datetime as dt
from typing import List, Dict

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
        return '<WeatherInfo ({} {})>'.format(self.date, self.time)


def past_n_days_weather(n) -> List[Dict[str, str]]:
    """Return averages of weather data for the past n days."""
    today_date = dt.date.today()
    past_n_days = [today_date - dt.timedelta(days=i) for i in range(1, n + 1)]

    # Query for the averages of stored weather data.
    weather_data_averages = (
        db.session.query(
            db.func.avg(WeatherInfo.humidity),
            db.func.avg(WeatherInfo.pressure_hg),
            db.func.avg(WeatherInfo.pressure_mb),
            db.func.avg(WeatherInfo.rain),
            db.func.avg(WeatherInfo.temperature),
        ).group_by(WeatherInfo.date)
    )

    info = []
    for date in past_n_days:
        # Retrieve the average weather data for a particular date.
        weather_info = (
            weather_data_averages
            .filter(WeatherInfo.date == date)
            .first()
        )
        if weather_info:  # if the data existed in the database
            info.append({
                'day': date.strftime('%A'),
                'humidity': f'{weather_info[0]:.1f}',
                'pressure_hg': f'{weather_info[1]:.1f}',
                'pressure_mb': f'{weather_info[2]:.1f}',
                'rain': f'{weather_info[3]:.1f}',
                'temperature': f'{weather_info[4]:.1f}',
            })
        else:  # if the data did not exist
            info.append({
                'day': date.strftime('%A'),
                'humidity': '-',
                'pressure_hg': '-',
                'pressure_mb': '-',
                'rain': '-',
                'temperature': '-',
            })

    return info


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
