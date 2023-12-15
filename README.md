# Data Scraper Project

This is a simple Python project that demonstrates how to scrape promo codes from a web page and provide a searchable interface using a web UI. The project is divided into three primary components: a scraper, a database interface, and a Flask web application.

## Requirements

- Python 3.6+
- pip for installing Python packages

## Setup

To set up and run this project, you will need to follow these steps:

1. Create a virtual environment (recommended):

```sh
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

2. Install the required dependencies:

```sh
pip install -r requirements.txt
```

3. Initialize the database:

```sh
python -m database.initialize_db
```

4. Run the scraper to populate the database with promo codes:

```sh
python -m scraper.data_scraper
```

5. Start the Flask web server:

```sh
python -m webui.app
```

Visit http://127.0.0.1:5000/ in your web browser to use the application.


## Project Structure
```
data-scraper-project/
│
├── scraper/
│   ├── __init__.py
│   └── data_scraper.py
│
├── database/
│   ├── __init__.py
│   ├── db_manager.py
│   └── initialize_db.py
│
├── webui/
│   ├── __init__.py
│   ├── app.py
│   └── templates/
│       └── search.html
│  
├── requirements.txt
└── README.md
```
## Usage

After you have completed the setup steps, you can use the web UI to search for promo codes. If you want to refresh the list of promo codes, stop the Flask server, re-run the scraper, and then start the server again.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments

This project was built for educational purposes and is not intended for production use.


