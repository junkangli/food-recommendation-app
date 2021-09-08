from flask import Flask, render_template

import query

application = Flask(__name__)

@application.route('/')
def index():
    data = []
    for area in query.list_all_areas():
        data.append({'area': area, 'count': query.count_meals_by_area(area)})
    return render_template('index.html', data=data)

if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()