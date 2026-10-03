from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()

@tool
def triple(num:float) -> float:
    """
    param num: a number to triple
    returns: the triple of the input number
    """
    return float(num) * 3

##here we are sending two tools. Tavile search and the above triple tool
tools = [TavilySearch(max_results=1), triple]
#tavily search description us prebuilt
#like triple you dont ahve to define. 
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0).bind_tools(tools)
##this is function calling
##here LLM vendor in this case Open AI is responsible for choosing the tool
