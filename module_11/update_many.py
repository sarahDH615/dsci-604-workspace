from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://sarahdhood_db_user:wILeFKWqYTGmrInM@cs618-blog.dwxex4z.mongodb.net/"
    "?retryWrites=true&w=majority&appName=cs618-blog",
    server_api = ServerApi('1')
)

# access airbnb db
db = client['sample_airbnb']
collection = db['listingsAndReviews']

search_filter = {'bedrooms': {'$gte': 10}}

for p in collection.find(search_filter):
    print(p['name'])
    print(p['minimum_nights'])

print('-'*15)
# update_many([where], [what to set])
# separate filters/keys by commas
collection.update_many(search_filter, {'$set': {'minimum_nights': 5}})

for p in collection.find(search_filter):
    print(p['name'])
    print(p['minimum_nights'])
