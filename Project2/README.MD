#PROJECT2

##PROJECT OVERVIEW
We we're assigned a project with the following instructions, feed in 2-3 urls that are stored inside a input text file and get back only the headings of business related articles, then store them in an output text file.


##Why is this helpful?
I will be going over exactly what you need to install in order to do something similiar that I accomplished, a simple webscraper. I was fairly shocked at how easy this is, this a vital skill to have in order to get data off the web and be able to store it locally and dynamically. It is incredibly useful and is something that I will use in order for projects of my own.

##Prerequisites
Have miniconda installed, some version of python, visual studio code, and git.

###Step by Step Instructions

1. Install both beautiful soup and requests
pip install beautifulsoup4
pip install requests

type both of these commands into your terminal, then put both of these lines at the top of your file.

```
import requests
from bs4 import BeautifulSoup
```

This is basically all that is needed in order to build something similiar to mine, it is incredibly straightforward and simple, you now have free reign over whatever website you want!

##How to build something similiar

I attacked this from a functions perspective, sure you could put everything in Main but that is way sloppier in my opinion, the thought in my head is that there are three critical sections. Reading the input file, parsing and scraping the data in order to find the headlines, and outputting those headlines into a new text file, here is how I attacked the inputting the file

```
def reading_urls(filename): 
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]
```

this function reads the text file and stores the url inside a list, removing any unnecessary whitepsace

```
def web_scraper(url): 
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'} 
    
    response = requests.get(url) 
    
    soup = BeautifulSoup(response.content, "html.parser") 
    
    if "ksdk.com" in url: 
        headlines1 = [titles.get_text(strip=True) for titles in soup.find_all('a', class_="headline-list__title")]
        headlines2 = [titles.get_text(strip=True) for titles in soup.find_all('h4', class_="story__title")]
        headlines3 = [titles.get_text(strip=True) for titles in soup.find_all('a', class_="story-list__title-link")]
        return headlines1 + headlines2 + headlines3
    if "apnews.com" in url: # AP news for loop that loops to find all headlines.
         return [titles.get_text(strip=True) for titles in soup.find_all('h3', class_='PagePromo-title')]
    
    
    return[]
```

this function creates a beautiful soup object as well as has a getpull to the url we passed in when reading the file, the "User-Agent" part basically spoofs our scraper as a user, that is what I believe at least, some websites have restrictions against webscrapers so that helps us against that

The loops check for the KSDK and APNews url's, which is the one we passed in through the text file, returning a list of headings depending on what class and html tag is found

```
def output_file(filename, headings):
    with open(filename, 'w', encoding='utf-8') as f:
        for headline in headings:
            f.write(headline + '\n')
```

this function is also very simply, it just outputs the headlines to a text file, passing in our filename as well as list with the headlines inside of it

```
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

```

This is main, which is where we combine all of our functions in order for a perfect scraper.

We first set two variables, one to the name of our input file and one to our output file. Then a empty list is made and calls our "reading_urls" function which reads from our input file

we then call a loop that finds all of the headlines and stores them, we also have an error checker just in case the list is empty, finally we output the headlines into a text file


That is all! I hope it seems fairly simply, as I believe it is, while simple, it is incredibly useful!