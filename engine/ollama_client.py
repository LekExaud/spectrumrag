import requests
import json

class OllamaClient:
    def __init__(self, base_url="http://localhost:11434", model="qwen2.5:3b"):
        self.base_url = base_url
        self.model = model

    def generate(self, prompt: str, stream: bool = False) -> str:
        url = f"{self.base_url}/api/generate"
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": stream
        }
        
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()["response"]

if __name__ == "__main__":
    client = OllamaClient()
    test_prompt = "Explain ITU Radio Regulations in one short sentence."
    print(f"Prompt: {test_prompt}\nResponse:")
    print(client.generate(test_prompt))