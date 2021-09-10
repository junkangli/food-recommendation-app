import requests

def list_all_areas():
    api_url = "https://www.themealdb.com/api/json/v1/1/list.php?a=list"
    response = requests.get(api_url)
    result = response.json()
    return [area['strArea'] for area in result['meals']]

def count_meals_by_area(area):
    api_url = f"https://www.themealdb.com/api/json/v1/1/filter.php?a={area}"
    response = requests.get(api_url)
    result = response.json()
    return len(result['meals'])

def list_all_categories():
    api_url = "https://www.themealdb.com/api/json/v1/1/list.php?c=list"
    response = requests.get(api_url)
    result = response.json()
    return [category['strCategory'] for category in result['meals']]

def list_all_ingredients():
    api_url = "https://www.themealdb.com/api/json/v1/1/list.php?i=list"
    response = requests.get(api_url)
    result = response.json()
    return [ingredient['strIngredient'] for ingredient in result['meals']]

def get_meals_by_main_ingredient(ingredient):
    api_url = f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredient}"
    response = requests.get(api_url)
    result = response.json()
    return [{'id': meal['idMeal'], 'name': meal['strMeal'], 'category': meal['strCategory']} for meal in result['meals']]

def search_meal_by_name(input):
    api_url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={input}"
    response = requests.get(api_url)
    result = response.json()
    return [{'id': meal['idMeal'], 'name': meal['strMeal'], 'category': meal['strCategory']} for meal in result['meals']]

def get_meal_by_id(idMeal):
    api_url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={idMeal}"
    response = requests.get(api_url)
    result = response.json()
    meal = result['meals'][0]
    return {
        'id': meal['idMeal'],
        'name': meal['strMeal'],
        'category': meal['strCategory'],
        'ingredients': get_ingredients(meal),
        'instructions': meal['strInstructions']
    }

def get_ingredients(meal):
    ingredients = []
    for k, v in meal.items():
        if k.startswith('strIngredient'):
            print(v)
            if v is not None and len(v) > 0:
                ingredients.append(v)
    return ingredients