"""Provides functions to download files from Google Drive."""

import requests

def download_file_from_gd(id, destination):
    """Downloads file from Google Drive to destination."""

    url = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(url, params={"id": id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {"id": id, "confirm": token}
        response = session.get(url, params=params, stream=True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    """Gets token required for download."""

    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

def save_response_content(response, destination):
    """Writes the data from the retrieved Google Drive file to destination."""

    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)