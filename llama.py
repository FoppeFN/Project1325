import ollama

file_path = r"C:\Users\Nrfop\OneDrive\Desktop\CS325NewP1\Project1real\input.txt"

client = ollama.Client()
with open(file_path, "r") as file:
    content = file.read()

    
model = "llama3.2:1b"
prompt = f"Give me a one word response for whether the headlines A, B, and C are positive negative or neutral, no explanation or context needed. {content}"

response = client.generate(model=model, prompt=prompt)

output_file = "outputllama.txt"

with open(output_file, "w") as file:
    file.write(response.response)

