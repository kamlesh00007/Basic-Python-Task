import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL of the web page to scrape
url = 'https://en.wikipedia.org/wiki/Main_Page'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the web page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract text from the web page
    text = soup.get_text()
    print("Text from the web page:")
    print(text)
    
    # Extract links from the web page
    links = []
    for link in soup.find_all('a', href=True):
        # Get the absolute URL of the link
        link_url = urljoin(url, link['href'])
        links.append(link_url)
    print("\nLinks from the web page:")
    print(links)
    
    # Extract images from the web page
    images = []
    for img in soup.find_all('img', src=True):
        # Get the absolute URL of the image
        img_url = urljoin(url, img['src'])
        images.append(img_url)
    print("\nImages from the web page:")
    print(images)
else:
    print("Failed to retrieve the web page. Status code:", response.status_code)
