from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    quote_data = None
    if request.method == 'POST':
        quote_data = get_quotes()
    return render_template('index.html', quote_data=quote_data)

def get_quotes():
    url = 'http://api.quotable.io/random'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {'quote': data['content'], 'author': data['author']}
    else:
        return {'quote': 'Ошибка получения цитаты.', 'author': ''}

if __name__ == '__main__':
    app.run()

