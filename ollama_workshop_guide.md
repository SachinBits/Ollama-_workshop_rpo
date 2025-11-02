# Ollama Workshop Guide
A comprehensive guide to getting started with Ollama for running large language models locally.

## 📋 Table of Contents
- Prerequisites
- Installation
- Getting Started
- CLI Commands
- Interaction Methods
- REST API
- UI Interface
- Python Integration
- Creating Custom Models
- Configuration
- Resources
- Troubleshooting

## Prerequisites
Before you begin, ensure you have:
- **Programming Knowledge** - Basic programming skills (Python recommended)
- **Development Environment** - A working development setup
- **Willingness to Learn** - Curiosity and enthusiasm to explore AI!

## Installation
1. Visit [ollama.com](https://ollama.com)
2. Click **Download** and select your operating system
3. Install the downloaded package
4. Browse available models by clicking **Models** in the navigation

## Getting Started
### Running Your First Model
```bash
ollama run deepseek-r1
```
This command will download (if needed) and start an interactive session with the model.

## CLI Commands
### Essential Commands
```bash
# List all installed models
ollama list

# Display help information
ollama help

# Remove a model
ollama rm <model_name>

# Download a model
ollama pull <model_name>

# Run a model
ollama run <model_name>
```
### Example Workflow
```bash
# Pull a model
ollama pull llama3.2

# Run the model
ollama run llama3.2

# Remove when done
ollama rm llama3.2
```

## Interaction Methods
### 1. REST API
Ollama provides a REST API running on `http://localhost:11434` for programmatic access.

#### Generate Response (Streaming)
```bash
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2",
  "prompt": "Write a parahraph on Agentic AI?"
}'
```

#### Generate Response (Non-Streaming)
```bash
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2",
  "prompt": "Tell me a fun fact about LangChain",
  "stream": false
}'
```

#### Chat with a Model
```bash
curl http://localhost:11434/api/chat -d '{
  "model": "llama3.2",
  "messages": [
    {
      "role": "user",
      "content": "Tell me a fun fact about Mozambique"
    }
  ],
  "stream": false
}'
```

### 2. UI Interface (Msty)
For those who prefer a graphical interface:
1. Visit [msty.app](https://msty.app)
2. Download and install for your operating system
3. Select **Setup Local AI**
4. Start chatting with your models!

### 3. Python Integration
#### Setup Your Environment
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install required packages
pip install requests ollama
```

#### Method A: Using Requests Library (Streaming)
```python
import requests
import json

url = "http://localhost:11434/api/generate"
payload = {
    "model": "deepseek-r1:1.5b",
    "prompt": "Explain about Langchain",
    "temperature": 0.3
}

response = requests.post(url, json=payload, stream=True)

if response.status_code == 200:
    print("Generated Response: ", end="", flush=True)
    
    for line in response.iter_lines():
        if line:
            decoded_line = line.decode('utf-8')
            result = json.loads(decoded_line)
            generated_text = result.get("response", "")
            print(generated_text, end="", flush=True)
else:
    print(f"Request failed with status code {response.status_code}: {response.text}")
```

#### Method B: Using Ollama Package (Chat)
```python
import ollama

response = ollama.chat(
    model="deepseek-r1:1.5b",
    messages=[
        {"role": "user", "content": "Explain about Langchain"}
    ],
)

print(response)
print(response["message"]["content"])
```

#### Method C: Using Ollama Package (Generate)
```python
import ollama

response = ollama.generate(
    model="mymodel",
    prompt="Explain about Langchain"
)

print(response["response"])
```

## Creating Custom Models
### Step 1: Create a Modelfile
Create a file named `Modelfile`:
```
FROM deepseek-r1:1.5b

# Set the temperature to 0.3 (higher is more creative)
PARAMETER temperature 0.3

SYSTEM """
You are a helpful assistant who always responds in a concise manner.
"""
```

### Step 2: Build Your Custom Model
```bash
# Create the model
ollama create mymodel -f ./Modelfile

# Run your custom model
ollama run mymodel
```

### Step 3: Test Your Model
```python
import ollama

response = ollama.generate(
    model="mymodel",
    prompt="Tell me about Python"
)

print(response["response"])
```

## Configuration
### Temperature Settings
Controls randomness in responses:
- `0.1 - 0.3`: More focused and deterministic
- `0.5 - 0.7`: Balanced creativity
- `0.8 - 1.0`: More creative and diverse

### System Prompts
Define your model's behavior:
```
SYSTEM """
You are an expert Python programmer who explains concepts clearly.
"""
```

### Other Parameters
```
PARAMETER num_ctx 4096        # Context window size
PARAMETER top_p 0.9           # Nucleus sampling
PARAMETER top_k 40            # Top-k sampling
```

## Resources
- Official Documentation: [Ollama GitHub](https://github.com/ollama)
- Model Library: [ollama.com/library](https://ollama.com/library)
- API Reference: API Documentation
- Python Package: Ollama-Python

## Troubleshooting
### Common Issues
**Ollama not responding?**
```bash
# Start Ollama service
ollama serve

# Check installed models
ollama list

# Verify API is running
curl http://localhost:11434/api/tags
```

**Model download issues:**
```bash
# Check available space
df -h

# Try pulling again
ollama pull <model_name>
```

**Port Conflicts**
- Default port: `11434`
- To change the port:
```bash
# Set environment variable
export OLLAMA_HOST=0.0.0.0:8080
ollama serve
```

## Contributing
Feel free to contribute to this guide! Submit issues or pull requests to improve the documentation.

## License
This workshop guide is provided as-is for educational purposes.

**Happy Modeling! 🚀**
For questions or support, visit the Ollama community.

