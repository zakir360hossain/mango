# import json
import pymongo


connection_url = "mongodb+srv://zakir:mongo123@cluster0.abqkq.mongodb.net/?retryWrites=true&w=majority"
app = Flask(__name__)
CORS(app)
client = pymongo.MongoClient(connection_url)

pool = client.get_database("pool")