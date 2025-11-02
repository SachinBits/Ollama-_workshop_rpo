from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage

class MyState(TypedDict):
    user_input: str
    response: str | None

def ollama_langchain_node(state: MyState):
    llm = ChatOllama(model="deepseek-r1:1.5b", temperature=0.3) 

    messages = [
        HumanMessage(content=state["user_input"])
    ]
    ai_msg = llm.invoke(messages)

    return {"response": ai_msg.content}

graph = StateGraph(MyState)

graph.add_node("chat_node", ollama_langchain_node)
graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

app = graph.compile()

if __name__ == "__main__":
    init_state = {"user_input": "Write a one-line poem about sunshine.", "response": None}
    result = app.invoke(init_state)

    print("✅ Final state:", result)
    print("\n💬 Model reply:")
    print(result["response"])


from IPython.display import Image, display
display(Image(app.get_graph(xray=True).draw_mermaid_png()))
