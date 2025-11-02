import ollama

response = ollama.chat(
    model="deepseek-r1:1.5b",
    messages=[
        {"role":"user", "content": "Explain about Langchain"}
    ],
)
print(response)
print(response["message"]["content"])