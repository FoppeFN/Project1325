import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, urls):
        self.urls = urls

    def fetch_and_save_headlines(self, output_filepath):
        headers = {'User-Agent': 'Mozilla/5.0'}

        with open(output_filepath, 'w', encoding='utf-8') as f:
            for url in self.urls:
                response = requests.get(url, headers=headers)
                soup = BeautifulSoup(response.content, "html.parser")

                url_headlines = []

                if "ksdk.com" in url:
                    url_headlines += [title.get_text(strip=True) for title in soup.find_all('a', class_="headline-list__title")]
                    url_headlines += [title.get_text(strip=True) for title in soup.find_all('h4', class_="story__title")]
                    url_headlines += [title.get_text(strip=True) for title in soup.find_all('a', class_="story-list__title-link")]

                elif "apnews.com" in url:
                    url_headlines += [title.get_text(strip=True) for title in soup.find_all('h3', class_='PagePromo-title')]

                # Write the first 5 headlines directly into the output file
                for headline in url_headlines[:5]:
                    f.write(headline + '\n')
