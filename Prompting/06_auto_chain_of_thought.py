from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = OpenAI(
    # api_key=os.environ["GEMINI_API_KEY"],
    # base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
You're an expert AI assistant that solves user queries using a simple
START -> PLAN -> OUTPUT process.

Rules:
- Always return valid JSON.
- Only perform ONE step at a time.
- The sequence is:
    1. START - acknowledge/understand the user's request
    2. PLAN - perform one planning/calculation step
    3. OUTPUT - give the final answer once the problem is solved
- You may use multiple PLAN steps.
- Do not give the final answer until you have completed enough PLAN steps.
- Once the problem is solved, return OUTPUT.
- Keep PLAN steps concise.

Output JSON format:

{
    "step": "START" | "PLAN" | "OUTPUT",
    "content": "string"
}
"""

print("\n\n")

message_history = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]

user_query = input("-> ")

message_history.append({
    "role": "user",
    "content": user_query
})

while True:

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_object"},
        messages=message_history
    )

    raw_result = response.choices[0].message.content

    try:
        parsed_result = json.loads(raw_result)
    except json.JSONDecodeError:
        print("Invalid JSON returned by model:")
        print(raw_result)
        break

    step = parsed_result.get("step")
    content = parsed_result.get("content")

    if step == "START":
        print("START:", content)

    elif step == "PLAN":
        print("PLAN:", content)

    elif step == "OUTPUT":
        print("OUTPUT:", content)
        break

    else:
        print("Unknown step:", parsed_result)
        break

    message_history.append({
        "role": "assistant",
        "content": raw_result
    })

    message_history.append({
        "role": "user",
        "content": "Continue to the next step."
    })

print("\n\n")
