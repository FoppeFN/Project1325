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
                    
    def analyze(self, texts):
        raise NotImplementedError("Use analyze_phi() or analyze_llama() instead.")
