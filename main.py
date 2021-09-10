import query
import rekognition

# for area in query.list_all_areas():
#     print(f'{area} || {query.count_meals_by_area(area)}')

#print(query.list_all_ingredients())

#print(query.get_meals_by_main_ingredient('Chicken'))

#print(query.get_meal_by_id('52940'))

#print(query.search_meal_by_name('wan'))

photo = "d:/temp/photo.jpg"
labels = rekognition.detect_labels_local_file(photo)
for label in labels:
    print (label['Name'] + ' : ' + str(label['Confidence']))
