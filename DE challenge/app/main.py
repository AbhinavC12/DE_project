from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import json
import os, subprocess
#for commit
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")



def load_country_data():
    try:
        with open("data/countries_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Country data file not found.")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Error decoding country data.")

country_data = load_country_data()

@app.get("/")
def root():
    with open("static/index.html") as f:
        return HTMLResponse(content=f.read())

@app.get("/countries")
def get_countries():
    """Returns the list of all countries available."""
    return {"countries": list(country_data.keys())}

@app.get("/countries/{country_name}")
def get_country(country_name: str):
    """Returns the specific data for a given country."""
    normalized_country_name = country_name.capitalize()
    country_info = country_data.get(normalized_country_name)
    if country_info:
        return country_info
    else:
        raise HTTPException(status_code=404, detail="Country not found")
