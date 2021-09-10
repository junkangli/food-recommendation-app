from flask import Flask, render_template, request

import query

application = Flask(__name__)

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

if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()