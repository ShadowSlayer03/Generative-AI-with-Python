from typing import Annotated

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict

load_dotenv()

llm = init_chat_model(
    model="gpt-6-luna",
    model_provider="openai"
)

class State(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot(state: State):
    print("Inside chatbot node:", state)
    print("\n")
    response = llm.invoke(state.get("messages"))
    return { "messages": [response]}

def sample_node(state: State):
    print("Inside sample_node node:", state)
    print("\n")
    return { "messages": ["Sample message appended"]}

graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("sample_node", sample_node)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", "sample_node")
graph_builder.add_edge("sample_node", END)

graph = graph_builder.compile()

updated_state = graph.invoke(State({"messages": ["Hi my name is Arjun"]}))
print("updated_state:", updated_state)
