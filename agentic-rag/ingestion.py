from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_unstructured import UnstructuredLoader
from langchain_pinecone import PineconeVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

urls = [
    "https://lilianweng.github.io/posts/2023-06-23-agent/",
    "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
    "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
]

# Load webpages
docs = [
    UnstructuredLoader(
        web_url=url, chunking_strategy="basic", max_characters=1000000
    ).load()
    for url in urls
]
# Flatten list
docs_list = [item for sublist in docs for item in sublist]

# Split into chunks
text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=250,
    chunk_overlap=0,
)

doc_splits = text_splitter.split_documents(docs_list)

# Embedding model
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

# Store in Pinecone
vectorstore = PineconeVectorStore.from_documents(
    documents=doc_splits,
    embedding=embeddings,
    index_name="agentic-rag",
)

# Retriever
retriever = vectorstore.as_retriever()