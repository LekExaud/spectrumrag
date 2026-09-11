import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

class AnthropicClient:
    def __init__(self, model: str = "claude-3-5-sonnet-20241022"):
        self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.model = model

    def generate(self, prompt: str, system_prompt: str = "") -> str:
        kwargs = {
            "model": self.model,
            "max_tokens": 1024,
            "messages": [{"role": "user", "content": prompt}]
        }
        if system_prompt:
            kwargs["system"] = system_prompt

        response = self.client.messages.create(**kwargs)
        # Anthropic content returns a typed block array
        return response.content[0].text

    def stream(self, prompt: str, system_prompt: str = ""):
        kwargs = {
            "model": self.model,
            "max_tokens": 1024,
            "messages": [{"role": "user", "content": prompt}]
        }
        if system_prompt:
            kwargs["system"] = system_prompt

        with self.client.messages.stream(**kwargs) as stream:
            for text in stream.text_stream:
                yield text

if __name__ == "__main__":
    client = AnthropicClient()
    sys_p = "You are a spectrum management specialist."
    user_p = "State the sub-6 GHz spectrum ranges for 5G NR."
    
    print("--- Anthropic Claude Response ---")
    print(client.generate(user_p, system_prompt=sys_p))