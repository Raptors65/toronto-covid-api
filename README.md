# toronto-covid-api

An API, supporting GET and POST requests, for COVID-19 data related to Toronto, Ontario.

## Installation
1. Fork and clone the git repository.
2. Install the required libraries: `apscheduler`, `bottle`, `beautifulsoup4`, `openpyxl`, `requests`.
3. Run `main.py`.
4. Now, you should be able to use the API with `http://localhost:8080/<feature ID>`.

## Current Features

### Daily Status
A daily summary, including total cases, probable/confirmed cases, and outbreaks.

### Communities
Includes total and recent data for each community, including long-term care homes and retirement homes.

### Schools
Includes student, staff, and resolved cases for each school and whether the school is open.

### Episode vs Reported Date
Includes resolved, active, and deceased, confirmed VOC, and screened positive VOC cases organized by episode and reported date.

## Planned Features

- Cases by outbreak type
- Toronto compared to other Ontario health units

## Known Issues

- Small typo in a date in a spreadsheet, like an additional space, will cause an error. While uncommon, this does occur on some days.
