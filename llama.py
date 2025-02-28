import ollama #imports ollama library

client = ollama.Client() #sets client to instance of ollama client
model = "llama3.2:1b" #sets the model to llama3.2:1b


with open("input.txt", "r") as file: #open input.txt and reads it line by line, with each line being an index in a list.
    prompt = file.readlines()
    
with open("outputllamabasic.txt", "w") as output_file, open ("junkllamabasic.txt", "w" ) as junk_file: #opens two files and sets them to write, one being the junk file, the other being the file with the output we care about.
    for language_output in prompt: #sets a for loop reading in the lines from input.txt
        response_prompt = ("Classify the following headline as Negative, Neutral, or Positive, provide only a one word response. The following sentence is the headline:" + language_output) #sets response_prompt to a question + the line we are feeding in, so in the first instance of the loop, the a line gets read in, then b line.
        response = client.generate(model=model, prompt=response_prompt) # this puts the response in which the client generates to a variable named response, we pass in the model and the prompt.
        # print(response.response) // for debugging purposes
        if response.response.lower() in ["positive", "negative", "neutral"]: #this simply makes the response.response to lower cause and then checks if it is one of our words we are looking for and if it is we print to our output_file, this code works perfectly since our model only prints in one word, our phi is a different case.
            output_file.write(response.response + "\n")
        else: #writes to junk file if any other word except "positive" "neutral" or "negative" is spotted (not really needed since model only prints one word).
            junk_file.write(response.response + "\n")
        
    

        



