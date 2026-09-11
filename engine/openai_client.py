import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class OpenAICloudClient:
    def __init__(self, model: str = "gpt-4o"):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = model

    def generate(self, prompt: str, system_prompt: str = "") -> str:
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.7
        )
        return response.choices[0].message.content

    def stream(self, prompt: str, system_prompt: str = ""):
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.7,
            stream=True
        )
        for chunk in response:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content

if __name__ == "__main__":
    client = OpenAICloudClient()
    sys_p = "You are a spectrum management specialist."
    user_p = "State the sub-6 GHz spectrum ranges for 5G NR."

    print("--- OpenAI GPT Response ---")
    print(client.generate(user_p, system_prompt=sys_p))