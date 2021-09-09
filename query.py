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

def list_all_ingredients():
    api_url = "https://www.themealdb.com/api/json/v1/1/list.php?i=list"
    response = requests.get(api_url)
    result = response.json()
    return [ingredient['strIngredient'] for ingredient in result['meals']]

def get_meals_by_main_ingredient(ingredient):
    api_url = f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredient}"
    response = requests.get(api_url)
    result = response.json()
    return [{'id': meal['idMeal'], 'name': meal['strMeal']} for meal in result['meals']]

def list_all_categories():
    api_url = "https://www.themealdb.com/api/json/v1/1/list.php?c=list"
    response = requests.get(api_url)
    result = response.json()
    return [category['strCategory'] for category in result['meals']]

def get_meal_by_id(idMeal):
    api_url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={idMeal}"
    response = requests.get(api_url)
    result = response.json()
    return [(meal['idMeal'], meal['strMeal'], meal['strCategory']) for meal in result['meals']]
