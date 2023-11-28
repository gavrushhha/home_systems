from flask import Flask, request
from bs4 import BeautifulSoup
import requests
import pandas as pd 

app = Flask(__name__)
df = pd.read_csv('habr.csv')
urls = df['url'].tolist()

@app.route('/parse', methods=['POST'])
def parse_data():
    data = request.get_json()
    url = urls[1] if urls else ''
    name = data.get('name')
    html_code = requests.get(url).text
    soup = BeautifulSoup(html_code, 'html.parser')
    title = soup.title.string if soup.title else 'No title found'
    meta_description_tag = soup.find('meta', attrs={'name': 'description'})
    meta_description = meta_description_tag.get('content') if meta_description_tag else 'No meta description found'

    parsed_data = {
        'url': url,
        'name': name,
        'parsed_info': {
            'title': title,
            'meta_description': meta_description
        }
    }

    return parsed_data

if __name__ == '__main__':
    app.run(port=5001)
