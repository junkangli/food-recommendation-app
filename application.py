import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

import query
import rekognition

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

application = Flask(__name__)
application.config['MAX_CONTENT_LENGTH'] = 1 * 1000 * 1000
application.config['UPLOAD_FOLDER'] = os.environ.get('UPLOAD_FOLDER', 'd:/temp/uploads')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@application.route('/')
def index():
    data = []
    for area in query.list_all_areas():
        data.append({'area': area, 'count': query.count_meals_by_area(area)})
    return render_template('index.html', data=data)

@application.route('/search-by-ingredients')
def search_by_ingredients():
    ingredients = query.list_all_ingredients()
    ingredient = request.args.get('ingredient')
    if ingredient:
        meals = query.get_meals_by_main_ingredient(ingredient)
        return render_template('search-by-ingredients.html', ingredients=ingredients, meals=meals)
    else:
        return render_template('search-by-ingredients.html', ingredients=ingredients)

@application.route('/search-by-description')
def search_by_description():
    search = request.args.get('search')
    if search:
        meals = query.search_meal_by_name(search)
        return render_template('search-by-description.html', meals=meals)
    else:
        return render_template('search-by-description.html')

@application.route('/meal')
def meal():
    id = request.args.get('id')
    meal = query.get_meal_by_id(id)
    return render_template('meal.html', meal=meal)

@application.route('/search-by-photo', methods=['GET', 'POST'])
def search_by_photo():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            print(f'photo posted {file.filename}')
            filename = secure_filename(file.filename)
            file.save(os.path.join(application.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('search_by_photo', filename=filename))
    filename = request.args.get('filename')
    if filename:
        labels = rekognition.detect_labels_local_file(os.path.join(application.config['UPLOAD_FOLDER'], filename))
        return render_template('search-by-photo.html', filename=filename, labels=labels)
    return render_template('search-by-photo.html')

if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()