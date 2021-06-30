import bottle
from bs4 import BeautifulSoup
from datetime import datetime
import json
import requests

# settings
cols = ["id", "name", "student_confirmed_cases", "staff_confirmed_cases", "resolved_cases", "is_open"]
types = [int, str, int, int, int, bool]
output_file = "schools.json"

def update():
    """Updates school data."""

    # getting the html page with data
    html_page = requests.get("https://docs.google.com/spreadsheets/d/1gEipMl79REabV5GPuJnPeziC3DbYhA92U_BxpzdKX_Y/htmlembed/sheet?gid=0").text
    soup = BeautifulSoup(html_page, "html.parser")

    # getting the rows of the table
    tbody = soup.find("tbody")
    entries = tbody.contents

    # the first row contains the date it was last updated
    date_row = entries[0]
    # getting the part after "last updated at" and ignoring .s
    as_of = date_row.td.get_text()[16:].replace(".", "").strip()
    # converting the 
    as_of_date = datetime.strptime(as_of, "%I:%M %p %B %d, %Y").strftime("%m/%d/%Y %H:%M:00")

    schools = []
    for school_row in entries[2:-3]:
        cells = [cell.get_text() for cell in school_row.contents]
        cells[5] = True if cells[5] == "Open" else False

        schools.append(dict(zip(cols, (types[i](j) if j else 0 for i, j in enumerate(cells)))))
    
    full_data = {"data": schools, "as_of": as_of_date}

    with open(output_file, "w") as f:
        json.dump(full_data, f)

@bottle.get("/schools")
@bottle.post("/schools")
def api():
    """Returns school data that matches parameters."""

    with open(output_file) as f:
        schools_data = json.load(f)
        for param, value in bottle.request.params.items():
            if param in cols:
                schools_data["data"] = list(filter(lambda x: str(x[param]) == value, schools_data["data"]))
    return {"result": schools_data, "success": True}