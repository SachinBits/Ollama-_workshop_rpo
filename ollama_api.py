import requests 
import json

url = "http://localhost:11434/api/generate"
payload = {
    "model": "deepseek-r1:1.5b",
    "prompt": "Explain about Langchain",
    "temperature": 0.3
}

response = requests.post(url,json=payload,stream=True)

if response.status_code == 200:
    print("Generated Response:",end="",flush=True)

    for line in response.iter_lines():
        if line:
            decoded_line = line.decode('utf-8')
            result= json.loads(decoded_line)
            generated_text = result.get("response","")
            print(generated_text, end="", flush=True)

else:
    print(f"Request failed with status code {response.status_code}: {response.text}")