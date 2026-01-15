
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from prompts import *

from langgraph.constants import END
from langgraph.graph import StateGraph

llm=ChatGroq(model="llama-3.3-70b-versatile")
from states import *

user_prompt="create a simple calculator web application"

def planner_agent(state: dict) -> dict:
    user_prompt=state["user_prompt"]
    response=llm.with_structured_output(Plan).invoke(planner_prompt(user_prompt))
    return {"plan":response}


graph=StateGraph(dict)
graph.add_node("planner",planner_agent)
graph.set_entry_point("planner")