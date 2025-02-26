import ollama

client = ollama.Client()
with open("input.txt", "r") as file:
    content = file.read()

    
model = "phi3:latest"
prompt = f"Give me a one word response for whether the headlines A, B, and C are positive negative or neutral, no explanation or context needed. {content}"

response = client.generate(model=model, prompt=prompt)

output_file = "outputphi.txt"

with open(output_file, "w", encoding="utf-8") as file:
    file.write(response.response)