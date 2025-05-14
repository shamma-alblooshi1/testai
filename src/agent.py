from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_ollama import OllamaLLM

# 👇 Define the model here (flake will detect it)
OLLAMA_MODEL = "mistral"

# Initialize the local model
llm = OllamaLLM(model=OLLAMA_MODEL)

# Prompt template (used repeatedly in the loop)
prompt = PromptTemplate.from_template("""
You are a professional assistant that writes emails.

Context: {context}
Tone: {tone}

Write a clear and appropriate email based on the context.
""")

# Chain together prompt + model
email_agent = prompt | llm

print("\n📬 Email Assistant Ready!")
print("Type your email context or 'exit' to quit.\n")

# Set tone once or prompt for it as well
tone = input("Preferred tone (e.g., formal, friendly): ").strip() or "formal"

# 🔁 Start interaction loop
while True:
    context = input("\n📝 Email context: ").strip()
    if context.lower() in {"exit", "quit"}:
        print("👋 Goodbye!")
        break

    query = {
        "context": context,
        "tone": tone
    }

    print("\n📧 Drafting email...\n")
    response = email_agent.invoke(query)
    print(response)
