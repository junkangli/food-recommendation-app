from flask import Flask, render_template, request

import query

application = Flask(__name__)

@application.route('/')
def index():
    data = []
    for area in query.list_all_areas():
        data.append({'area': area, 'count': query.count_meals_by_area(area)})
    return render_template('index.html', data=data)

@application.route('/search-by-ingredients', methods=('GET', 'POST'))
def search_by_ingredients():
    ingredients = query.list_all_ingredients()
    ingredient = request.args.get('ingredient')
    if ingredient:
        meals = []
        for meal in query.get_meals_by_main_ingredient(ingredient):
            mealDetail = query.get_meal_by_id(meal['id'])
            meals.append({
                'id': mealDetail['id'],
                'name': mealDetail['name'],
                'category': mealDetail['category']
            })
        return render_template('search-by-ingredients.html', ingredients=ingredients, meals=meals)
    else:
        return render_template('search-by-ingredients.html', ingredients=ingredients)

if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()