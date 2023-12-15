# data-scraper-project/webui/app.py

from flask import Flask, render_template, request
from database.db_manager import search_promo_codes, initialize_database

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    search_term = ''
    results = []
    if request.method == 'POST':
        search_term = request.form.get('search_term', '')
        results = search_promo_codes(search_term)
    return render_template('search.html', results=results, search_term=search_term)

if __name__ == '__main__':
    app.run(debug=True)
