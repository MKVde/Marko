import requests
from bs4 import BeautifulSoup
import os

# URL of the main anime page
url = "https://witanime.com/anime/my-home-hero/"

# Send a GET request to the URL and get the response
response = requests.get(url)

# Use BeautifulSoup to parse the response HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all the episode links on the page
episode_links = soup.select(".episodes-card-title a")

# Create a directory to store the text files if it doesn't exist
dir_path = "C:\\Users\\abdir\\OneDrive\\Desktop\\Web Dev\\Web Scraping Learn\\Extract mega link from the website"
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

# Extract anime name from URL
anime_name = url.split('/')[-2]

# Loop through each episode URL
for episode_link in episode_links:
    episode_url = episode_link["href"]

    # Make a GET request to the episode page
    response = requests.get(episode_url)

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all HTML elements containing "mega" link
    mega_links = soup.find_all('a', href=lambda href: href and 'mega' in href)

    # Extract the second link from the list of "mega" links
    if len(mega_links) >= 2:
        download_link = mega_links[1]['href']
        episode_num = episode_link.text.split(' ')[-1]
        print(f"Download link for Episode {episode_num}: {download_link}")

        # Write the download link to a text file
        filename = f"{anime_name}.txt"
        file_path = os.path.join(dir_path, filename)
        with open(file_path, "a") as f:
            f.write(f"Episode {episode_num}: {download_link}\n")
    else:
        episode_num = episode_link.text.split(' ')[-1]
        print(f"No 'mega' link found in Episode {episode_num}")

        # Write an error message to a text file
        filename = f"{anime_name}.txt"
        file_path = os.path.join(dir_path, filename)
        with open(file_path, "a") as f:
            f.write(f"No 'mega' link found in Episode {episode_num}\n")
