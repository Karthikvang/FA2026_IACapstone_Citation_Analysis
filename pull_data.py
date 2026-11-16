import requests
import pandas as pd
import numpy as np
from config import API_KEY, API_EMAIL


''' 
This file has 2 main aims:

Scrape the NaNDA webpage for the DOI identification numbers of the articles on the ISR's 
website. This will avoid needing manual input regarding what documents to look for since the script will automatically 
be compiling them.

Use the list of NaNDA page DOI numbers to find articles citing them and save the demographic information for later use. 
This will later be used for the dashboard
'''

TARGET_DOI = "https://doi.org/10.3886/ICPSR38506.v2"
OPENALEX_WORKS_URL = "https://api.openalex.org/works"

params = {
    "search": f'"{TARGET_DOI}"',
    "corpus": "all",
    "api_key": API_KEY,
    "mailto": API_EMAIL,
}

resp = requests.get(OPENALEX_WORKS_URL, params=params, timeout=30)
resp.raise_for_status()
results = resp.json().get("results", [])

results = pd.DataFrame(results)

results.to_csv("test_output_1.csv", index=False)