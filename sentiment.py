from abc import ABC, abstractmethod
import ollama

class SentimentAnalyzer(ABC): #abstract method
    @abstractmethod
    def analyze(self, texts):
        pass

class DoubleLLM(SentimentAnalyzer):
    def __init__(self): #simply initializes the client, as well as the two models for both of our functions.
        self.client = ollama.Client(host="host.docker.internal")
        self.phi_model = "phi3:latest"
        self.llama_model = "llama3.2:1b"

    def analyze_phi(self, texts):
        junk_output = ""
        
        with open("sentiments_phi.txt", "w", encoding="utf-8") as output_file: #opens the output.phi text file
            for language_output in texts: #starts a for loop that goes through each prompt, starting with a and ending with c.
                response_prompt = f"is this statement: {language_output} positive, negative, or neutral? answer in one word." # sets what we are prompting the llm
                response = self.client.generate(model=self.phi_model, prompt=response_prompt)
                #print(response.response)

                if response.response.lower() in ["positive", "negative", "neutral"]:  #similiar to our llama code, if the first word that is printed out by our llm, it will be saved to our parsed data file and a new line will be printed, if not then the else will be activated.
                    output_file.write(response.response + "\n")
                else:
                    split_response = str(response.response.lower()).split()  #sets a new variable called split response, that first converts it to a string from a list and divides our strings into substrings.
                    #print(split_response)

                    for parsed_data in split_response:  #creates a for loop to iterate through our string of split responses, which could be a very long paragraph of data.
                        if parsed_data in ["positive", "negative", "neutral", "positive.", "negative.", "neutral.", "positive,", "negative,", "neutral,"]:  #if that word is found, the if block is activated
                            output_file.write(parsed_data + "\n")  #writes the data to our parsed data file
                            split_response.remove(parsed_data)  #removes that word from our split_response, as we have already found it and do not want to find it again.
                            break  #breaks the for loop and moves to print out the rest of the garbage text, as we have found connotation word.

                    output_rebuild = "" #initializes output_rebuild 
                    for rebuild in split_response:
                       #print(rebuild)
                        output_rebuild = output_rebuild + " " + rebuild #this line rebuilds the garbage text data that the LLM is outputting

                    output_rebuild += "\n"  # in case the LLM writes two long worded responses, this will create a new line in the junk file between the two
                    junk_output += output_rebuild #adds the outputted rebuilt to our junk

        # Save junk separately
        with open("junk_phi.txt", "w", encoding="utf-8") as junk_file:
            junk_file.write(junk_output)


    def analyze_llama(self, texts):
        with open("sentiments_llama.txt", "w", encoding="utf-8") as output_file, \
             open("junk_llama.txt", "w", encoding="utf-8") as junk_file: #open input.txt and reads it line by line, with each line being an index in a list, also opens the junk llama text file.

            for language_output in texts:  #sets a for loop reading in the lines from input.txt
                response_prompt = "Classify the following headline as Negative, Neutral, or Positive, provide only a one word response. The following sentence is the headline: " + language_output #sets response_prompt to a question + the line we are feeding in, so in the first instance of the loop, the a line gets read in, then b line.
                response = self.client.generate(model=self.llama_model, prompt=response_prompt)  # this puts the response in which the client generates to a variable named response, we pass in the model and the prompt.
                #print(response.response)

                if response.response.lower() in ["positive", "negative", "neutral"]: #this simply makes the response.response to lower cause and then checks if it is one of our words we are looking for and if it is we print to our output_file, this code works perfectly since our model only prints in one word, our phi is a different case.
                    output_file.write(response.response + "\n")
                    
                else:  #writes to junk file if any other word except "positive" "neutral" or "negative" is spotted (not really needed since model only prints one word).
                    junk_file.write(response.response + "\n")
                    
    def analyze(self, texts):#error test if you just use the basic analyze function.
        raise NotImplementedError("Use analyze_phi() or analyze_llama() instead.")
