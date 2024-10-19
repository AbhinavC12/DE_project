1. Run the Scraper This will scrape data from the World Bank and save it in data/countries_data.json.

-- python scraper.py or python -m app.scraper

2. Run the FastAPI Application

-- uvicorn main:app --reload

Access the API at http://127.0.0.1:8000

Note: 

-- Please ensure that the data directory exists before running the scraper, as the script will attempt to save the scraped JSON data there.

-- If you have any suggestions or questions regarding the code or functionality, feel free to reach out!

-- I am working on deploying the code in a single run without executing multiple files separately.