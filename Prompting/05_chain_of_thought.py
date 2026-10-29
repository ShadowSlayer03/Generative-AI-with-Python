from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = OpenAI()

SYSTEM_PROMPT="""
You're an expert AI assistant in resolving user queries using chain of thought
You work on START, PLAN and OUTPUT steps.
You need to first PLAN what needs to be done. The PLAN can be multiple steps.
Once you think enough PLAN has been done, finally you can give an OUTPUT.

Rules:
    - Strictly follow the given JSON output format
    - Only run one step at a time
    - The sequence of steps is START(where user gives an input), PLAN(that can be multiple times) and finally OUTPUT(which is going to the displayed to the user)

    Output JSON format:
        {{
            "step" : "START" | "PLAN" | "OUTPUT", "content": "string"
        }}

    Example:
        START: Hey, can you solve 2 + 3 * 5 / 10 ?
        PLAN: { "step": "START", "content": "Write a code to add n numbers in python?" }
        PLAN: { "step": "PLAN", "content": "Seems like user is interested in this math problem" }
        PLAN: { "step": "PLAN", "content": "This can be solved using the BODMAS method" }
        PLAN: { "step": "PLAN", "content": "First we must divide 5 and 10" }
        PLAN: { "step": "PLAN", "content": "That gives 3 multiplied by 0.5" }
        PLAN: { "step": "PLAN", "content": "Then we should add 2 and 1.5" }
        PLAN: { "step": "PLAN", "content": "Final answer comes off as 3.5" }
        OUTPUT: { "step": "OUTPUT", "content": "The answer is 3.5" }
"""

response = client.chat.completions.create(
    model="gpt-4o",
    response_format={"type": "json_object"},
    messages=[
        {   "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": "Write a code to add n numbers in python?"
        },
        {
            "role": "assistant",
            "content": json.dumps({
                "step": "PLAN",
                "content": "The user wants a Python program to add 'n' numbers. I should design a solution that accepts either a list of numbers or takes input dynamically from the user."
            },
            # Keep appending the previous output to get a new output
            )
        }
    ]
)

for choice in response.choices:
    print(choice.message.content)
    print("\n")
