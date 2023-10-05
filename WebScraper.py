import requests
from bs4 import BeautifulSoup

# Define the URL of the web page you want to scrape
url = 'https://rajgulshan.blogspot.com/2017/05/sync-quote-line-item-custom-fields-with.html'  # Replace with your desired URL

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the web page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract all the text from the HTML document
    plain_text = soup.get_text()

    # Print or process the plain text as needed
    print(plain_text)
else:
    print(f"Failed to fetch the web page (Status Code: {response.status_code})")

# Close the response to release resources
response.close()
