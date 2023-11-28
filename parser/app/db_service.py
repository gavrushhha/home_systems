from flask import Flask, request
from pymongo import MongoClient
import pandas as pd

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['habr_db']
collection = db['parsed_data']
df = pd.read_csv('habr.csv')
urls = df['url'].tolist()

@app.route('/parse', methods=['POST'])
def parse_data_and_save():
    data = request.get_json()
    url = urls[0] if urls else ''
    name = data.get('name')
    parsed_data = {
        'url': url,
        'name': name,
        'parsed_info': {
        }
    }
    collection.insert_one(parsed_data)

    return {'message': 'Data parsed and saved to database'}

if __name__ == '__main__':
    if 'habr_db' not in client.list_database_names():
        print("Creating database 'habr_db' and collection 'parsed_data'")
        client.habr_db.create_collection('parsed_data')

    app.run(port=5001)
