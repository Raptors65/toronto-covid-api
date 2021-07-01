"""Converts episode date data from the daily status Excel file into JSON and deals with requests."""

import bottle
from datetime import datetime
from daily_cases import excel_file
import json
from openpyxl import load_workbook

# settings
cols = ["date", "recovered_cases", "active_cases", "deceased_cases"]
output_file = "episode_date.json"

def update():
    """Updates data on cases by episode date."""

    # loads the downloaded excel file (from daily_cases.py)
    wb = load_workbook(excel_file)
    episode_date_data = wb["Cases by Episode Date"]
    status = []
    for row in episode_date_data.iter_rows(min_row=2, values_only=True):
        # date is a datetime object so it must be converted to str
        status.append(dict([(cols[0], row[0].strftime("%m/%d/%Y")), *zip(cols[1:], row[1:])]))
    
    # "as of" date
    data_date = wb["Data Note"]["A2"].value[11:]
    formatted_date = datetime.strptime(data_date, "%B %d, %Y").strftime("%m/%d/%Y")

    # combining the data and the date
    full_data = {"data": status, "as_of": formatted_date}

    # storing in JSON file
    with open(output_file, "w") as f:
        json.dump(full_data, f)

@bottle.get("/episode_date")
@bottle.post("/episode_date")
def api():
    """Returns COVID-19 data by episode date that matches parameters."""

    with open(output_file, "r") as f:
        episode_date = json.load(f)
        # filtering out data
        for param, value in bottle.request.params.items():
            if param in cols:
                episode_date["data"] = list(filter(lambda x: str(x[param]) == value, episode_date["data"]))
    return {"result": episode_date, "success": True}