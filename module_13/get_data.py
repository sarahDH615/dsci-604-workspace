from pymongo import MongoClient
from pymongo.server_api import ServerApi

from var_reader import username, password

client = MongoClient(
    f"mongodb+srv://{username}:{password}@cs618-blog.dwxex4z.mongodb.net/"
    "?retryWrites=true&w=majority&appName=cs618-blog",
    server_api = ServerApi('1')
)

def get_values_in_search(coll, filters, to_display, cols, remove_id=True):
    '''display columns for specific search'''
    if remove_id:
        to_display['_id'] = 0
    for r in coll.find(
        filters,
        to_display
    ):
        for c in cols:
            if r[c] and r[c] is not None and r[c] != '':
                print(r[c])

# 1. sample_airbnb : listingsAndReviews
airbnb_db = client['sample_airbnb']
listing_collection = airbnb_db['listingsAndReviews']

# # Name of all properties in the United States
print('Names of properties in the United States:\n')
get_values_in_search(
    listing_collection,
    {'address.country_code': 'US'},
    {'name': 1}, ['name']
)
print('-'*20)
print('Names of properties with a minimum 3 night stay:\n')
# # Name of all properties with a minimum night stay of 3
get_values_in_search(
    listing_collection,
    {'minimum_nights': '3'},
    {'name': 1}, ['name']
)
print('-'*20)
print('Names and descriptions of properties with at least 5 bedrooms:\n')
# # Name and description of all properties with at least 5 bedrooms
get_values_in_search(
    listing_collection,
    {'beds': {'$gte': 5}},
    {'name': 1, 'description': 1}, ['name', 'description']
)


# 2. sample_mflix : movies
mflix_db = client['sample_mflix']
movies_collection = mflix_db['movies']

# Title of movies with an imdb rating of 7 or more
print('-'*20)
print('Titles of films with an imdb rating of at least 7:\n')
get_values_in_search(
    movies_collection,
    {'imdb.rating': {'$gte': 7}},
    {'title': 1}, ['title']
)
# Title of drama (genre) movies released in 2007
print('-'*20)
print('Titles of drama films released in 2007:\n')
get_values_in_search(
    movies_collection,
    {'genres': 'Drama', 'year': 2007},
    {'title': 1}, ['title']
)
# Title of PG-13 (rated) movies that have won at least 3 awards
print('-'*20)
print('Titles of PG-13 films that won at least 3 awards:\n')
get_values_in_search(
    movies_collection,
    {'awards.wins': {'$gte': 3}, 'rated': 'PG-13'},
    {'title': 1}, ['title']
)

# 3. sample_restaurants : restaurants
restaurants_db = client['sample_restaurants']
restaurants_collection = restaurants_db['restaurants']

# Name of all restaurants in Brooklyn (borough)
print('-'*20)
print('Names of all restaurants in Brooklyn:\n')
get_values_in_search(
    restaurants_collection,
    {'borough': 'Brooklyn'},
    {'name': 1}, ['name']
)
# Name and borough of all American cuisine restaurants in Queens (borough)
print('-'*20)
print('Names and boroughs of all restaurants in Queens:\n')
get_values_in_search(
    restaurants_collection,
    {'borough': 'Queens', 'cuisine': 'American'},
    {'name': 1}, ['name']
)




