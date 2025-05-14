from transformers import pipeline

# Define independent agents
planner = pipeline("text2text-generation", model="google/flan-t5-base")
researcher = pipeline("text2text-generation", model="google/flan-t5-base")
analyst = pipeline("text2text-generation", model="google/flan-t5-base")

# Independent tasks
task_1 = "Create a 3-step plan to reduce plastic waste in the ocean."
task_2 = "Summarize the key differences between supervised and unsupervised learning."
task_3 = "Evaluate the pros and cons of using renewable energy in urban areas."

# Run agents independently
plan_result = planner(task_1, max_new_tokens=100)[0]['generated_text']
research_result = researcher(task_2, max_new_tokens=100)[0]['generated_text']
analysis_result = analyst(task_3, max_new_tokens=100)[0]['generated_text']

# Display results
print("🧠 Planner Result:\n", plan_result)
print("\n📚 Researcher Result:\n", research_result)
print("\n📊 Analyst Result:\n", analysis_result)
