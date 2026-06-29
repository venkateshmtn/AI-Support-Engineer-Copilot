from app.llm.ollama_client import llm

response = llm.invoke(
    "What causes payment failures?"
)

print(response.content)