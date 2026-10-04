from dotenv import load_dotenv
from langgraph.graph import MessagesState
#store the key of the messages. Agents keep track human and ai.
from langgraph.prebuilt import ToolNode
#Execute tools.  Whats the last message ai or human message. 

from react import llm, tools
#this is from the react file that we created earlier.
load_dotenv()

SYSYEM_MESSAGE="""
You are a helpful assistant that can use tools to answer questions.
"""

def run_agent_reasoning(state: MessagesState) -> MessagesState:
    """
    Run the agent reasoning node.
    """
    response = llm.invoke([{"role": "system", "content": SYSYEM_MESSAGE}, *state["messages"]])
    #role is system and the entire system message is passed on |
    #[
    #SystemMessage("You are...")
    #HumanMessage("What is the capital of France?")
    #both are passed together
    #"Take the system instruction and prepend it to the current message history."
    return {"messages": [response]}


tool_node = ToolNode(tools)