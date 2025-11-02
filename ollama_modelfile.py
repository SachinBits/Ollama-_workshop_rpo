import ollama

response=ollama.generate(model="mymodel",prompt="Explain about Langchain")

print(response["response"])