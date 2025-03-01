import ollama #import ollama library

client = ollama.Client() #sets client up
model = "phi3:latest" #sets model to phi3


with open("input.txt", "r") as file: #opens up input.txt
    prompt = file.readlines() #reads prompt into a list, where each line is an index in the list.

    
with open("outputphi.txt", "w", encoding = "utf-8") as output_file: #opens the output.phi text file
    for language_output in prompt: #starts a for loop that goes through each prompt, starting with a and ending with c.
        response_prompt = f"is this statement: {language_output} positive, negative, or neutral? answer in one word." # sets what we are prompting the llm
        response = client.generate(model=model, prompt=response_prompt)
        print(response.response) 
        if response.response.lower() in ["positive", "negative", "neutral"]: #similiar to our llama code, if the first word that is printed out by our llm, it will be saved to our parsed data file and a new line will be printed, if not then the else will be activated.
            output_file.write(response.response + "\n")
        else:
            split_response = str(response.response.lower()).split() #sets a new variable called split response, that first converts it to a string from a list and divides our strings into substrings.
            print(split_response) 
            for parsed_data in split_response: #creates a for loop to iterate through our string of split responses, which could be a very long paragraph of data.
                    if parsed_data in ["positive","negative","neutral"]: #if that word is found, the if block is activated
                        output_file.write(parsed_data + "\n") #writes the data to our parsed data file
                        split_response.remove(parsed_data) #removes that word from our split_response, as we have already found it and do not want to find it again.
                        break #breaks the for loop and moves to print out the rest of the garbage text, as we have found connotation word.
            output_rebuild = "" #initializes output_rebuild 
            for rebuild in split_response:
                print(rebuild) 
                output_rebuild = output_rebuild + " " + rebuild #this line rebuilds the garbage text data that the LLM is outputting
            output_rebuild += "\n" # in case the LLM writes two long worded responses, this will create a new line in the junk file between the two
            print(output_rebuild) 

            junk_file = open("junkphi.txt", "w", encoding = "utf-8")
            junk_file.write(output_rebuild)
            junk_file.close()