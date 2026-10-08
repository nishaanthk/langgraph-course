from dotenv import load_dotenv

load_dotenv()

from graph.graph import app

if __name__ == "__main__":
    print("Hello Advanced RAG")
    #print(app.invoke(input={"question": "what is agent memory?"}))
    result = app.invoke(
        input={"question": "What is Ferrari F40?"}
    )

    print(result["generation"])