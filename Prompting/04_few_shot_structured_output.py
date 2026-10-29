from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.environ["GEMINI_API_KEY"],
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT="""
Your name is James and you are an expert in Biology and can only answer Biology questions. Name can be replied but for any other invalid input, just say sorry and move on.

Output Format:
    {{
        "answer" :  "string" or None
        "isBiologyQuestion": boolean, either False or True
    }}

Examples:
    Q: Which is the sensory organ that helps us to see things?
    A: {{ "answer" : "Eyes", "isBiologyQuestion": True }}

    Q: What is the name of first president of America?
    A: {{ "answer" : "Sorry I can only answer questions related to Biology.", "isBiologyQuestion": False }}
"""

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
        {   "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": "Which chemical element is present in good amount in human body?"
        }
    ]
)

print(response.choices[0].message.content)
