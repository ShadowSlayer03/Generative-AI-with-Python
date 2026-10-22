from typing import Annotated

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.mongodb import MongoDBSaver
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from pymongo import MongoClient
from typing_extensions import TypedDict

load_dotenv()

llm = init_chat_model(
    model="gpt-6-luna",
    model_provider="openai"
)

class State(TypedDict):
    messages: Annotated[list, add_messages]

def compile_graph_with_checkpointer():
    DB_URI = "mongodb://admin:admin@localhost:27017/langgraph?authSource=admin"
    client = MongoClient(DB_URI)
    checkpointer = MongoDBSaver(client)
    return graph_builder.compile(checkpointer=checkpointer)

def chatbot(state: State):
    response = llm.invoke(state.get("messages"))
    return { "messages": [response]}

graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

graph_with_checkpointer = compile_graph_with_checkpointer()

config = {
    "configurable": {
        "thread_id": "arjun"  #user_id
    }
}

for chunk in graph_with_checkpointer.stream(
    State({"messages": ["Who and where am I?"]}),
    config=config,
    stream_mode="values"
):
    chunk["messages"][-1].pretty_print()
