from scraper import Scraper
from sentiment import DoubleLLM

def read_urls(filepath):
    with open(filepath, "r") as file:
        return [line.strip() for line in file if line.strip()]

def main():
    urls = read_urls("URLs.txt")
    scraper = Scraper(urls)
    scraper.fetch_and_save_headlines("scraped_headlines.txt")

    with open("scraped_headlines.txt", "r", encoding="utf-8") as f:
        headlines = [line.strip() for line in f if line.strip()]

    analyzer = DoubleLLM()
    analyzer.analyze_phi(headlines)
    analyzer.analyze_llama(headlines)

if __name__ == "__main__":
    main()

