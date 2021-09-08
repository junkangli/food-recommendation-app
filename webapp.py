from flask import Flask, render_template

import query

app = Flask(__name__)

@app.route('/')
def index():
    data = []
    for area in query.list_all_areas():
        data.append({'area': area, 'count': query.count_meals_by_area(area)})
    return render_template('index.html', data=data)
