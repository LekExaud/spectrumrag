# engine/test_tools.py
import json
from engine.openai_client import OpenAICloudClient
from engine.schema import SPECTRUM_TOOL_DEFINITION
from engine.tools import AVAILABLE_TOOLS

if __name__ == "__main__":
    client = OpenAICloudClient()
    
    messages = [{"role": "user", "content": "Can you look up the C-band allocation for Region 1 spanning 3300 to 3800 MHz?"}]
    
    response = client.client.chat.completions.create(
        model=client.model,
        messages=messages,
        tools=[SPECTRUM_TOOL_DEFINITION],
        tool_choice="auto"
    )
    
    message = response.choices[0].message
    if message.tool_calls:
        tool_call = message.tool_calls[0]
        func_name = tool_call.function.name
        func_args = json.loads(tool_call.function.arguments)
        
        print(f"Model requested tool: {func_name}")
        print(f"Arguments parsed: {func_args}")
        
        if func_name in AVAILABLE_TOOLS:
            tool_output = AVAILABLE_TOOLS[func_name](**func_args)
            print(f"\nTool Execution Result:\n{tool_output}")