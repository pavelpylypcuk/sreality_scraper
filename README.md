# sreality_scraper

This app uses the Scrapy framework within Python in order to scrape first 500 items off sreality.cz (specifically, in category flats/sell).

The app furthermore uses PostgreSQL database in order to store the scraped data and renders it via a Flask server at http://127.0.0.1:8080/.

To run this app, simply type the 'docker-compose up' command from the project's root folder.
