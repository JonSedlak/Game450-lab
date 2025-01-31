from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

from ollama import chat
from util.llm_utils import pretty_stringify_chat, ollama_seed as seed

# Add you code below
sign_your_name = 'Jonathan Sedlak'
model = 'llama3.2'
messages = [{'role': 'system', 'content': 'You are a DND Master'}]
options = {'temperature': 0.5, 'max_tokens': 100} # Temperature: Low = Accurate, High = Creative


# But before here.

options |= {'seed': seed(sign_your_name)}

# Chat loop
while True:
  # Send message to Chat Model and store assistant response in Response
  response = chat(model=model, messages=messages, stream=False, options=options)
  # Add your code below
  #-----------------------------------------------------------

  print(f'Agent: {response.message.content}')
  messages.append({'role': 'assistant', 'content': response.message.content})

  # Prompt for user input
  message = {'role': 'user', 'content': input('You: ')}
  messages.append(message)

  #-----------------------------------------------------------
  # But before here.
  if messages[-1]['content'] == '/exit':
    break

# Save chat
with open(Path('lab03/attempts.txt'), 'a') as f:
  file_string  = ''
  file_string +=       '-------------------------NEW ATTEMPT-------------------------\n\n\n'
  file_string += f'Model: {model}\n'
  file_string += f'Options: {options}\n'
  file_string += pretty_stringify_chat(messages)
  file_string += '\n\n\n------------------------END OF ATTEMPT------------------------\n\n\n'
  f.write(file_string)