import os

from dotenv import load_dotenv

from llama_index.core import Settings, StorageContext, load_index_from_storage
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.openai_like import OpenAILike

from pathlib import Path
env_path = Path(__file__).resolve().parent.parent / ".env"

load_dotenv(env_path)

Settings.embed_model = HuggingFaceEmbedding("BAAI/bge-small-zh-v1.5")

Settings.llm = OpenAILike(
    model="glm-4.7-flash-free",
    api_key=os.getenv("AIHUBMIX_API_KEY"),
    api_base="https://aihubmix.com/v1",
    is_chat_model=True
)

persist_path = "./llamaindex_index_store"

strorage_context = StorageContext.from_defaults(persist_dir=persist_path)
loaded_index = load_index_from_storage(strorage_context)
query_engine = loaded_index.as_query_engine()

print("\n=== 执行相似性搜索 ===")
query = "LlamaIndex是做什么的？"
result = query_engine.query(query)
print(result)

print("\n=== 使用向量检索器进行相似性搜索 ===")
retriever = loaded_index.as_retriever(similarity_top_k=2)
similar_docs = retriever.retrieve(query)
for i, doc in enumerate(similar_docs):
    print(f"{i+1}. {doc.text}")
