import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, urls):
        self.urls = urls

    def fetch_and_save_headlines(self, output_filepath):
        headers = {'User-Agent': 'Mozilla/5.0'} #this allows our parser to act like a user, so we do not get some error or something

        with open(output_filepath, 'w', encoding='utf-8') as f:
            for url in self.urls: #loop that just runs for how many urls there are.
                response = requests.get(url, headers=headers)  #requests.get use the requests library and makes a get requests through the passed in URL
                soup = BeautifulSoup(response.content, "html.parser") #creates a Beautiful Soup object, passes in our parser and also gets all of the content from the passed in website url

                url_headlines = [] #just a list of headlines that we continuously add onto.

                if "ksdk.com" in url: # this for loop is for the KSDK.com business journal, the reason I have 3 loops is because their headlines do not all use the same class or html object, while AP News does.
                    url_headlines += [title.get_text(strip=True) for title in soup.find_all('a', class_="headline-list__title")]
                    url_headlines += [title.get_text(strip=True) for title in soup.find_all('h4', class_="story__title")]
                    url_headlines += [title.get_text(strip=True) for title in soup.find_all('a', class_="story-list__title-link")]

                elif "apnews.com" in url:# AP news for loop that loops to find all headlines.
                    url_headlines += [title.get_text(strip=True) for title in soup.find_all('h3', class_='PagePromo-title')]

                # Write the first 5 headlines directly into the output file
                for headline in url_headlines[:5]:
                    f.write(headline + '\n')
