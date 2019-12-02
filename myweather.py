from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myweather.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class WeatherInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, nullable=False)
    humidity = db.Column(db.String(50))
    pressure_hg = db.Column(db.String(50))
    pressure_mb = db.Column(db.String(50))
    rain = db.Column(db.String(50))
    temperature = db.Column(db.String(50))

    def __repr__(self):
        return '<WeatherInfo ({})>'.format(self.time)


@app.route('/')
def index():
    return render_template('index.html', current_temperature=69)
