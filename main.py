from scraper import Scraper
from sentiment import DoubleLLM #importing both of our other files, which are made with classes using inheritance.

def read_urls(filepath): #function to read urls, line by line.
    with open(filepath, "r") as file:
        return [line.strip() for line in file if line.strip()]

def main():
    urls = read_urls("URLs.txt") #pass in our url to our read_urls function
    scraper = Scraper(urls) #pass in our urls to our scraper function
    scraper.fetch_and_save_headlines("scraped_headlines.txt") #saves our scraped headlines to this .txt file.

    with open("scraped_headlines.txt", "r", encoding="utf-8") as f: #opens the scraped_headlines.txt file and reads line by line.
        headlines = [line.strip() for line in f if line.strip()]

    analyzer = DoubleLLM() #calls an instance of our DoubleLLM class
    analyzer.analyze_phi(headlines) #calls our phi function, this function already prints out to our sentiments_phi.txt file
    analyzer.analyze_llama(headlines) #calls our phi function, this function already prints out to our sentiments_phi.txt file

if __name__ == "__main__":
    main()

