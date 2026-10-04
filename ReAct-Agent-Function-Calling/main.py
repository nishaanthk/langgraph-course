from dotenv import load_dotenv

from langchain_core.messages import HumanMessage
from langgraph.graph import MessagesState, StateGraph,END
#receive any state object. stagegraph

from nodes import run_agent_reasoning, tool_node

load_dotenv()

AGENT_REASON="agent_reason"
ACT= "act"
LAST = -1
##last is to check the previous message


def should_continue(state: MessagesState) -> str:
    if not state["messages"][LAST].tool_calls:
        return END#no more tool call end
    return ACT#if tool call return act 

flow = StateGraph(MessagesState)
#Create a graph whose state follows MessagesState
flow.add_node(AGENT_REASON, run_agent_reasoning) #adding a node called agent reason
flow.set_entry_point(AGENT_REASON)##by above we are defining whats the entry .
flow.add_node(ACT, tool_node) #we are adding atool node.

flow.add_conditional_edges(AGENT_REASON, should_continue, {
    END:END,
    ACT:ACT}) 
#a conditional edge where it ends or continues based on tool calls status

flow.add_edge(ACT, AGENT_REASON)  
#It specifically sends execution from the tool node back to the reasoning node, creating the loop.

app = flow.compile() #we are compiling the graph
app.get_graph().draw_mermaid_png(output_file_path="flow.png")

if __name__ == "__main__":
    print("Hello ReAct LangGraph with Function Calling")
    res = app.invoke({"messages": [HumanMessage(content="What is the temperature in Tokyo? List it and then triple it")]})
    #invoking the compiled graph to start the process ##if temperature is not explicit
    #it gets all the details related to weather for example
    print(res["messages"][LAST].content)# Prints the text content of the last message 