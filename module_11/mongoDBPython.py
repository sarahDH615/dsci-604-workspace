from pymongo import MongoClient
from pymongo.server_api import ServerApi

from var_reader import username, password

client = MongoClient(
    f"mongodb+srv://{username}:{password}@cs618-blog.dwxex4z.mongodb.net/"
    "?retryWrites=true&w=majority&appName=cs618-blog",
    server_api = ServerApi('1')
)
# test connection
# print(client.list_database_names())

# access mflix db
db = client['sample_mflix']
collection = db['movies']
# testing connection
# print(collection.find_one())

# printing all the titles
# note how the keys must be strings now
# for m in collection.find({}, {'_id': 0, 'title': 1}):
# filter to year 2010
for m in collection.find({'year': 2010}, {'_id': 0, 'title': 1}):
    print(m)
