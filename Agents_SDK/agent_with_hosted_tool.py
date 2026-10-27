from agents import Agent, Runner, WebSearchTool
from dotenv import load_dotenv
from typing_extensions import Any

load_dotenv()

tool_agent = Agent[Any](
    name="Hello World Agent",
    instructions="You are an agent which greets the user and helps them answer using emojis in a funny way",
    tools=[
        WebSearchTool() # Hosted Tools by OpenAI team
    ]
)

result = Runner.run_sync(tool_agent, "Hey There, My name is Khalil so analyze arjunnambiar.dev and tell me what is it abt?")
print(result.final_output)
