1. Method Used for Web Scraping

-- Requests and BeautifulSoup: I made good use of the requests library to grab web pages, and I used BeautifulSoup to parse the HTML data. That combination is a common and productive method of screen scraping.

-- User-Agent Handling: I did remember to set a user-agent in the headers, which is always a good idea to avoid possible blocks by sites.

-- Session Management: By using a Session object, I was able to improve performance through the reuse of the underlying TCP connection, which I found to be a nice touch.

-- Dynamic URL Generation: I used urljoin to construct the full URLs accurately so that I could scrape the right URLs.

2. Data Storage and ETL Process

-- Data Structure: It's all stored in a dictionary with the country names as the keys, so it's really easy to look up data for a particular country.

-- JSON Storage: I chose to save the data to a JSON file (countriesdata.json), which is a straightforward and efficient way to store structured data, allowing easy access for the API.

-- ETL Process: The process is effectively handled in the scraping function, where I extract (fetch data from the web), transform (process and structure it), and load (write it to a JSON file) the data. I know I need to go back and add more error handling to my ETL process to make it as bulletproof as possible.

3. Data Chosen to Show on the API

I have selected six key indicators for each country:

-- Poverty headcount ratio at $2.15 a day (2017 PPP)  of population).

-- Life expectancy at birth, total (years)

-- Population, total

-- Population growth (annual %)

-- Net migration

-- Human Capital Index (HCI) (scale 0-1)


4. Readability and Performance of the Code

-- Code Structure: I ensured that the separation of concerns is well-managed, with the FastAPI app and scraping function in separate files for enhanced readability and maintainability.

-- Variable Naming: Most of my variable names are descriptive, which aids in following the flow of the program. Such as countrydata, and indicator_items, those are good names for variables.

-- Performance Considerations: I implemented time.sleep(randint(1, 8) to mitigate the risk of being rate-limited by the target site. But, depending on the number of requests, I might want to change this or look into asynchronous scraping if the site allows it.