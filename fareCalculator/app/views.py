from flask import render_template
from app import app

@app.route('/')
def index():
    base_fare = 10  # Hardcoded base fare value
    per_km_fare = 5  # Hardcoded per kilometer fare value
    return render_template('index.html', base_fare=base_fare, per_km_fare=per_km_fare)
