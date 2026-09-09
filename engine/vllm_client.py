from openai import OpenAI

class OpenAICompatibleClient:
    def __init__(self, base_url="http://localhost:1234/v1", api_key="lm-studio", model="qwen2.5-3b-instruct"):
        # LM Studio doesn't enforce API keys, but the OpenAI client expects a non-empty string
        self.client = OpenAI(base_url=base_url, api_key=api_key)
        self.model = model

    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a telecommunications engineering assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content

if __name__ == "__main__":
    client = OpenAICompatibleClient()
    
    test_prompt = "What is the primary role of the ITU Radiocommunication Sector (ITU-R)?"
    print(f"Prompt: {test_prompt}\n")
    try:
        result = client.generate(test_prompt)
        print(f"Response:\n{result}")
    except Exception as e:
        print(f"Connection Error: {e}")
        print("\nMake sure your LM Studio local server is running on http://localhost:1234!")