from gd_download import download_file_from_gd

# settings
gd_id = "11KF1DuN5tntugNc10ogQDzFnW05ruzLH"
excel_file = "daily_cases.xlsx"

def update():
    """Updates daily case data."""

    download_file_from_gd(gd_id, excel_file)