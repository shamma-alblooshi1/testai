from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_ollama import OllamaLLM

# Use a local LLM like mistral
llm = OllamaLLM(model="mistral")

# Prompt template for email writing
prompt = PromptTemplate.from_template("""
You are a professional assistant that writes emails.

Context: {context}
Tone: {tone}

Write a clear and appropriate email based on the context.
""")

# Chain the prompt into the LLM
email_agent = prompt | llm

# Example input
query = {
    "context": "Apologize to a client for submitting a report late and assure them it will be sent tomorrow.",
    "tone": "formal"
}

# Run agent
response = email_agent.invoke(query)

# Output
print("\n📧 Email Draft:\n")
print(response)


