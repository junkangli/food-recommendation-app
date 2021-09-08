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


for area in list_all_areas():
    print(f'{area} || {count_meals_by_area(area)}')

