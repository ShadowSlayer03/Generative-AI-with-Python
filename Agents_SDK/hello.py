from agents import Agent, Runner
from dotenv import load_dotenv
from typing_extensions import Any

load_dotenv()

hello_agent = Agent[Any](
    name="Hello World Agent",
    instructions="You are an agent which greets the user and helps them answer using emojis in a funny way"
)

result = Runner.run_sync(hello_agent, "Hey There, My name is Khalil and I am like a happy meal. In fifa I am defender")
print(result.final_output)
