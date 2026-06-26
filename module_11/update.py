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

search_filter = {'name': 'Horto flat with small garden'}

for p in collection.find(search_filter):
    print(p['weekly_price'])

# update_one([where], [what to set])
collection.update_one(search_filter, {'$set': {'weekly_price': 1000.00}})

for p in collection.find(search_filter):
    print(p['weekly_price'])
