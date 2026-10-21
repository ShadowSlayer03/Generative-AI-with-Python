import os
from typing import Literal, Optional

from dotenv import load_dotenv
from langgraph.graph import END, START, StateGraph
from openai import OpenAI
from typing_extensions import TypedDict

load_dotenv()

client = OpenAI()

gemini_client = OpenAI(
    api_key=os.environ["GEMINI_API_KEY"],
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


class State(TypedDict):
    user_query: str
    llm_output: Optional[str]
    is_good: Optional[bool]

def chatbot(state: State):
    print("\n" + f"chatbot Node state: {state}")
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": state.get("user_query")}
        ]
    )

    state['llm_output'] = response.choices[0].message.content
    return state

def evaluate_response(state: State) -> Literal["chatbot_gemini", "end_node"]:
    print("\n" + f"evaluate_response Node state: {state}")
    if False:
        return "end_node"

    return "chatbot_gemini"

def chatbot_gemini(state: State):
    print("\n" + f"chatbot_gemini Node state: {state}")
    response = gemini_client.chat.completions.create(
        model="gemini-3.5-flash",
        messages=[{"role": "user", "content": state.get("user_query")}]
    )
    state['llm_output'] = response.choices[0].message.content
    return state


def end_node(state: State):
    print("\n" + f"end_node Node state: {state}")
    return state

graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("chatbot_gemini", chatbot_gemini)
graph_builder.add_node("end_node", end_node)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_conditional_edges("chatbot", evaluate_response)
graph_builder.add_edge("chatbot_gemini", "end_node")
graph_builder.add_edge("end_node", END)

graph = graph_builder.compile()
updated_state = graph.invoke(State({"user_query": "What is 3+4?"}))
print(f"Updated state: {updated_state}")
