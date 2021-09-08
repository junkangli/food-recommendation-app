import query

for area in query.list_all_areas():
    print(f'{area} || {query.count_meals_by_area(area)}')

#print(query.get_meals_by_main_ingredient('Chicken'))

#print(query.get_meal_by_id('52940'))
