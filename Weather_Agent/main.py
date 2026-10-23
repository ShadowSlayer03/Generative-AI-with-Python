import os

from structured_agent import call_agent_parsed
from agent import call_agent
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

def main():
    user_query = input("-> ")
    # call_agent(user_query, client)
    call_agent_parsed(user_query,client)


main()
