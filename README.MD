# PROJECT2

## Prequsities

Just use the same exact environment that you built upon from project1 and project2, but just download pytest using this command.

```
pip install pytest
```

this should be the only library that you need to install, you also need to install docker container if you plan putting everything in a docker container.

```
https://www.docker.com/products/docker-desktop/
```

Go to this website and follow all steps, it is very straightforward. Finally make sure Docker Desktop is open, I will go into the details of how to put it in a docker container soon.

## How I combined everything

There are basically 3 main files that I have created that represent Project1, Project2 and Project3. Scraper.py is the file that represents what we did in Project 2. Except I made the function under a class named Scraper. I then named two functions that are represented here.

```
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
```

Next, for Project 1, this is where I use inheritance, it is a bit more complicated than the modularization and classifiction of Project2.

I made one file, called sentiment.py, which is the file that the headlines will be fed into and then given a positive, negative, or neutral sentiment.

```
from abc import ABC, abstractmethod
import ollama

class SentimentAnalyzer(ABC):
    @abstractmethod
    def analyze(self, texts):
        pass

class DoubleLLM(SentimentAnalyzer):
    def __init__(self):
        self.client = ollama.Client(host="host.docker.internal")
        self.phi_model = "phi3:latest"
        self.llama_model = "llama3.2:1b"

    def analyze_phi(self, texts):
        junk_output = ""
        
        with open("sentiments_phi.txt", "w", encoding="utf-8") as output_file:
            for language_output in texts:
                response_prompt = f"is this statement: {language_output} positive, negative, or neutral? answer in one word."
                response = self.client.generate(model=self.phi_model, prompt=response_prompt)
                #print(response.response)

                if response.response.lower() in ["positive", "negative", "neutral"]:
                    output_file.write(response.response + "\n")
                else:
                    split_response = str(response.response.lower()).split()
                    #print(split_response)

                    for parsed_data in split_response:
                        if parsed_data in ["positive", "negative", "neutral", "positive.", "negative.", "neutral.", "positive,", "negative,", "neutral,"]:
                            output_file.write(parsed_data + "\n")
                            split_response.remove(parsed_data)
                            break

                    output_rebuild = ""
                    for rebuild in split_response:
                       #print(rebuild)
                        output_rebuild = output_rebuild + " " + rebuild

                    output_rebuild += "\n"
                    junk_output += output_rebuild

        # Save junk separately
        with open("junk_phi.txt", "w", encoding="utf-8") as junk_file:
            junk_file.write(junk_output)


    def analyze_llama(self, texts):
        with open("sentiments_llama.txt", "w", encoding="utf-8") as output_file, \
             open("junk_llama.txt", "w", encoding="utf-8") as junk_file:

            for language_output in texts:
                response_prompt = "Classify the following headline as Negative, Neutral, or Positive, provide only a one word response. The following sentence is the headline: " + language_output
                response = self.client.generate(model=self.llama_model, prompt=response_prompt)
                #print(response.response)

                if response.response.lower() in ["positive", "negative", "neutral"]:
                    output_file.write(response.response + "\n")
                    
                else:
                    junk_file.write(response.response + "\n")
```

As you see at the top, I imported ABC and abstract method in order to successfully make our class and inheritance structure.

I then created a abstract method and made two functions, one for each model. Then basically jut copy and pasted my code from Project1 into this file, it is fairly straight forward. If you are using a docker container, when setting ollama as the host, you HAVE to have this in your code.

```
self.client = ollama.Client(host="host.docker.internal")
```

This allows docker to connect back to your host machine, all while running Ollama locally when you installed it for project1.

Finally, I created main.py in order to combine everything into one simple file, simply calling each function when necessary in order to get the curated result.



### How to use pytorch.

### How to setup a dockerfile



### Command to build and run docker
```
docker build -t cs325finalproject .      
docker run --rm -v "${PWD}:/project3" cs325finalproject    
```

Obviously change the final folder and directory to wherever everything is held to whatever you have it as. Just use the run command everytime you want to run the program and you are finished!