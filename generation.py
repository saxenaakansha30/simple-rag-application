from langchain_community.llms import ollama

def get_response(prompt):
  llm = ollama.Ollama(model="llama3:latest")
  response = llm.invoke(prompt)

  return response
