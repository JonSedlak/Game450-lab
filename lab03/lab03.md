# Prompt Engineering Process

## Step 1

### Intention

> What is the improvement that you intend to make?

- I want the model to be able to give me DND advice since I have never played it before

### Action/Change

> Why do you think this action/change will improve the agent?

- What I have done is change the system role and tweaked the temperature.
- The system role now says that you are a dungeon master

### Result

> What was the result?

- The result of this is that the agent will now respond more in character and percisely with DND questions
- It was able to tell me what this game was in great detail

### Reflection/Analysis of the result.

> Why do you think it did or did not work?

- I think that changing the system role is going to be the biggest part in this.
- Doing so I think acts as a 'prompt' for the agent.

# Prompt Engineering Process

1. Added user input and have it loop
2. Loop is broken and cannot enter in user input after 1st try. It keeps using the orginal message over and over unless I force quit.
3. Fixed the loop isue. Attempts.txt is now generating
4. Tried adding an intital statement. did not really work
5. Changed the temperature and system role content to more accurate
6. Went back to original conditions. Added an if statement to check for original message. Works now
7. Decided to get rid of If Else statement for initial message. Changed the system content to: You are a DND master
8. **I now have a better understanding how ollama works and the flow of series of messages**

## DISCLAIMER

### GitHub Account got hacked and deleted

**I had this project locally saved on my machine so I copied the files over and pasted them into a fresh git clone of the project from profremote**

## Ollama install:

- pip install ollama
- pip install llama
- llama pull ollama 3.2

- ollama run llama3.2
