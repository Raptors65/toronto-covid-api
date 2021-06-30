"""Downloads the daily Toronto COVID-19 update from Google Drive."""

from gd_download import download_file_from_gd

# Google Drive file with data
# https://drive.google.com/file/d/11KF1DuN5tntugNc10ogQDzFnW05ruzLH/view
gd_id = "11KF1DuN5tntugNc10ogQDzFnW05ruzLH"
# target Excel file
excel_file = "daily_cases.xlsx"

def update():
    """Updates daily case data."""
    
    download_file_from_gd(gd_id, excel_file)