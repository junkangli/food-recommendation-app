import requests

api_url = "https://www.themealdb.com/api/json/v1/1/list.php?a=list"
response = requests.get(api_url)
result = response.json()
areas = [area['strArea'] for area in result['meals']]
print(areas)