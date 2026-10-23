import requests
import json
from pydantic import BaseModel, Field
from typing import Optional

def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"

    return "Something went wrong!"


SYSTEM_PROMPT="""
You're an expert AI assistant in resolving user queries using chain of thought
You work on START, PLAN and OUTPUT steps.
You need to first PLAN what needs to be done. The PLAN can be multiple steps.
You can also call a TOOL to get things done, if you dont have the required capability to perform what the user requires.
Once you think enough PLAN has been done, finally you can give an OUTPUT.

Rules:
    - Strictly follow the given JSON output format
    - Only run one step at a time
    - The sequence of steps is START(where user gives an input), PLAN(that can be multiple times) or TOOL(also can be multiple times) and finally OUTPUT(which is going to the displayed to the user)

Tools available:
    - Function get_weather(city: str) that takes a city name and can fetch the current weather of that city using a weather API.
    - It returns a string either 'Something went wrong!' or replies with the current weather in the city

Output JSON format:
    {{
        "step" : "START" | "PLAN" | "OUTPUT" | "TOOL", "content": "string", "tool": "string", "input" | "output" : "string"
    }}

Example:
    START: Hey, can you solve 2 + 3 * 5 / 10 ?
    PLAN: { "step": "PLAN", "content": "Seems like user is interested in this math problem" }
    PLAN: { "step": "PLAN", "content": "This can be solved using the BODMAS method" }
    PLAN: { "step": "PLAN", "content": "First we must divide 5 and 10" }
    PLAN: { "step": "PLAN", "content": "That gives 3 multiplied by 0.5" }
    PLAN: { "step": "PLAN", "content": "Then we should add 2 and 1.5" }
    PLAN: { "step": "PLAN", "content": "Final answer comes off as 3.5" }
    OUTPUT: { "step": "OUTPUT", "content": "The answer is 3.5" }

Example:
    START: Hey, can you get the weather of New York ?
    PLAN: { "step": "PLAN", "content": "The user wants to know the current weather of New York" }
    PLAN: { "step": "PLAN", "content": "First let me check if I can get the weather from my knowledge" }
    PLAN: { "step": "PLAN", "content": "Weather is dynamic and can vary so I cannot get the latest information" }
    PLAN: { "step": "PLAN", "content": "Searching for a tool, awesome, I can call the get_weather tool here!" }
    PLAN: { "step": "TOOL", "tool": "get_weather", "input": "New York" }
    PLAN: { "step": "TOOL", "tool": "get_weather", "output": "The weather in New York is Mist +16°C" }
    OUTPUT: { "step": "OUTPUT", "content": "The current weather in New York is misty with a temp of 16°C" }
"""

class MyOutputFormat(BaseModel):
    step: str = Field(..., description="The ID of the ")
    content: Optional[str] = Field(None, description="The optional string content for the step")
    tool: Optional[str] = Field(None, description="The ID of the tool to call")
    input: Optional[str] = Field(None, description="The input params of the tool")
    output: Optional[str] = Field(None, description="The output params of the tool")

def call_agent_parsed(user_query:str, client):
    print("\n\n")

    message_history = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    message_history.append({
        "role": "user",
        "content": user_query
    })

    while True:
        response = client.chat.completions.parse(
            model="gpt-4o-mini",
            response_format=MyOutputFormat,
            messages=message_history,
        )

        parsed_result = response.choices[0].message.parsed

        step = parsed_result.step
        content = parsed_result.content

        if step == "START":
            print("START:", content)

        elif step == "PLAN":
            print("PLAN:", content)

        elif step == "TOOL":
            tool = parsed_result.tool
            input_val = parsed_result.input or None
            output_val = parsed_result.output or None
            print("TOOL:", tool)
            if input_val:
                print("TOOL INPUT:", input_val)
                if tool == "get_weather":
                    result = get_weather(input_val)
                    message_history.append({
                        "role": "assistant",
                        "content": parsed_result.model_dump_json()
                    })
                    message_history.append({
                        "role": "user",
                        "content": json.dumps({"step": "TOOL", "tool": "get_weather", "output": result})
                    })
                    continue
            if output_val:
                print("TOOL OUTPUT:", output_val)


        elif step == "OUTPUT":
            print("OUTPUT:", content)
            break

        else:
            print("Unknown step:", parsed_result)
            break

        message_history.append({
            "role": "assistant",
            "content": parsed_result.model_dump_json()
        })

        message_history.append({
            "role": "user",
            "content": "Continue to the next step."
        })

    print("\n\n")
