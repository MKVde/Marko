import requests
from bs4 import BeautifulSoup

# URL of the main anime page
url = "https://witanime.com/anime/my-home-hero/"

# Send a GET request to the URL and get the response
response = requests.get(url)

# Use BeautifulSoup to parse the response HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all the episode links on the page
episode_links = soup.select(".episodes-card-title a")

# Loop through each episode link
for episode_link in episode_links:
    episode_url = episode_link['href']
    
    # Make a GET request to the episode page
    response = requests.get(episode_url)

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all HTML elements containing "mega" link
    mega_links = soup.find_all('a', href=lambda href: href and 'mega' in href)

    # Extract the second link from the list of "mega" links
    if len(mega_links) >= 2:
        download_link = mega_links[1]['href']
        print(f"Download link for {episode_url}: {download_link}")
    else:
        print(f"No 'mega' link found in {episode_url}")
