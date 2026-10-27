import asyncio
from typing import Annotated

from agents import Agent, Runner, ToolSearchTool
from agents.decorators import tool
from dotenv import load_dotenv

load_dotenv()


@tool(defer_loading=True)
def get_customer_profile(
    customer_id: Annotated[str, "The customer ID to look up."],
) -> str:
    """Fetch a CRM customer profile."""
    return f"profile for {customer_id}"


async def main():
    agent = Agent(
        name="Operations assistant",
        model="gpt-5.6-sol",
        instructions="Imagine you are a CRM assistant and have all the CRM tools with you.",
        tools=[get_customer_profile, ToolSearchTool()],
    )

    result = await Runner.run(agent, "Look up customer_42 and get his profile.")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
