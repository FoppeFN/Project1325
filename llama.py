import ollama

client = ollama.Client()
model = "llama3.2:1b"


with open("input.txt", "r") as file:
    prompt = file.readlines()

    
with open("outputllama.txt", "w") as output_file:
    for language_output in prompt:
        response_prompt = ("Classify the following headline as Negative, Neutral, or Positive, provide only a one word response, this is the headline:" + language_output)
        response = client.generate(model=model, prompt=response_prompt)
        output_file.write(response.response + "\n")

        



