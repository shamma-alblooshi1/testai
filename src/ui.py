import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading

from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

# Set model name
OLLAMA_MODEL = "mistral"

# Setup LangChain
llm = OllamaLLM(model=OLLAMA_MODEL)
prompt = PromptTemplate.from_template("""
You are a professional assistant that writes emails.

Context: {context}
Tone: {tone}

Write a clear and appropriate email based on the context.
""")
chain = prompt | llm

# GUI logic
def generate_email():
    context = context_input.get("1.0", tzk.END).strip()
    tone = tone_var.get()

    if not context:
        messagebox.showwarning("Missing Input", "Please enter email context.")
        return

    # Disable button while processing
    generate_btn.config(state="disabled")
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, "⏳ Generating email...")

    def task():
        try:
            response = chain.invoke({"context": context, "tone": tone})
            output_box.delete("1.0", tk.END)
            output_box.insert(tk.END, response)
        except Exception as e:
            output_box.delete("1.0", tk.END)
            output_box.insert(tk.END, f"❌ Error: {str(e)}")
        finally:
            generate_btn.config(state="normal")

    # Run LLM generation in a thread
    threading.Thread(target=task, daemon=True).start()

# GUI setup
root = tk.Tk()
root.title("AI Email Writing Assistant")
root.geometry("700x500")

frame = ttk.Frame(root, padding=10)
frame.pack(fill="both", expand=True)

ttk.Label(frame, text="Email Context:").pack(anchor="w")
context_input = scrolledtext.ScrolledText(frame, height=6)
context_input.pack(fill="x")

ttk.Label(frame, text="Select Tone:").pack(anchor="w", pady=(10, 0))
tone_var = tk.StringVar(value="formal")
for tone_option in ["formal", "friendly", "assertive"]:
    ttk.Radiobutton(frame, text=tone_option.capitalize(), variable=tone_var, value=tone_option).pack(anchor="w")

generate_btn = ttk.Button(frame, text="✉️ Generate Email", command=generate_email)
generate_btn.pack(pady=10)

ttk.Label(frame, text="Generated Email:").pack(anchor="w")
output_box = scrolledtext.ScrolledText(frame, height=12)
output_box.pack(fill="both", expand=True)

# Run the GUI
root.mainloop()
