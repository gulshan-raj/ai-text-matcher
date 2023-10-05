import requests
from bs4 import BeautifulSoup

def get_plain_text_from_url(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the web page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract all the text from the HTML document
            plain_text = soup.get_text()
            print(f"Texts are {plain_text}")
            # Close the response to release resources
            response.close()

            return plain_text
        else:
            return f"Failed to fetch the web page (Status Code: {response.status_code})"
    except Exception as e:
        return f"Error: {str(e)}"


