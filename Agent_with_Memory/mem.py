import json
import os

from dotenv import load_dotenv
from mem0 import Memory
from openai import OpenAI

load_dotenv()

client = OpenAI()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
USER_ID = "arjun"

config = {
    "version": "v1.1",
    "embedder": {
        "provider": "openai",
        "config": {
            "api_key": OPENAI_API_KEY,
            "model": "text-embedding-3-small"
        }
    },
    "llm": {
        "provider": "openai",
        "config": {
            "model": "gpt-5-mini",
            "temperature": 0.1
        }
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333
        },
    },
}

memory_client = Memory.from_config(config)

while True:
    user_query = input("> ")

    search_memory = memory_client.search(query=user_query, filters={"user_id": USER_ID})

    memories = [
        f"ID: {mem.get('id')} \nMemory: {mem.get('memory')}" for mem in search_memory["results"]
    ]

    print("Found memories:", memories)

    SYSTEM_PROMPT = f"""
        Here is the context about the user:
        {json.dumps(memories)}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            { "role": "system", "content": SYSTEM_PROMPT },
            { "role": "user", "content": user_query }
        ]
    )

    ai_response = response.choices[0].message.content
    print("AI response:", ai_response)

    messages = [
        {"role": "user", "content": user_query},
        {"role": "assistant", "content": ai_response}
    ]

    memory_client.add(
        messages,
        user_id=USER_ID
    )
