#This is my webscraper, I used beautifulsoup as well as requests in order to pull the website, both of these are essential to use a webscraper

import requests
from bs4 import BeautifulSoup

def reading_urls(filename): #function opens file and readings line by line until there is nothing left in the file
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def web_scraper(url): # function that will actually scrape headings from our websites, has checks depending on what websites are passed through
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'} #this allows our parser to act like a user, so we do not get some error or something
    
    response = requests.get(url) #requests.get use the requests library and makes a get requests through the passed in URL
    
    soup = BeautifulSoup(response.content, "html.parser") #creates a Beautiful Soup object, passes in our parser and also gets all of the content from the passed in website url
    
    if "ksdk.com" in url: # this for loop is for the KSDK.com business journal, the reason I have 3 loops is because their headlines do not all use the same class or html object, while AP News does.
        headlines1 = [titles.get_text(strip=True) for titles in soup.find_all('a', class_="headline-list__title")]
        headlines2 = [titles.get_text(strip=True) for titles in soup.find_all('h4', class_="story__title")]
        headlines3 = [titles.get_text(strip=True) for titles in soup.find_all('a', class_="story-list__title-link")]
        return headlines1 + headlines2 + headlines3
    if "apnews.com" in url: # AP news for loop that loops to find all headlines.
         return [titles.get_text(strip=True) for titles in soup.find_all('h3', class_='PagePromo-title')]
    
    
    return[]

#this function simply prints out the headlines we found from the two websites
def output_file(filename, headings):
    with open(filename, 'w', encoding='utf-8') as f:
        for headline in headings:
            f.write(headline + '\n')
    

def main():
    #sets our input and output file to our respective files
    input_file = "URLs.txt"
    output_file_scraped = "headingsoutput.txt"
    
    #creates a empty list and passes our urls into our reading function that we created
    urls = reading_urls(input_file)
    scraped_headlines = []
    
    for url in urls: #created a for loop that passes in our urls one by one and then returns the list of headlines that it scraped, saves the previous list with scraped headlines, which is initially empty
        headlines = web_scraper(url)
        scraped_headlines = scraped_headlines + headlines
    
    #if the list is empty, simply return a message saying no headlines were found
    if not scraped_headlines:
        print("No headlines were found")
        
    #outputs the headlines to our output file
    output_file(output_file_scraped, scraped_headlines)
    
if __name__ == "__main__":
    main()
