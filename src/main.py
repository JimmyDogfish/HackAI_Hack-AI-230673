#Import Bureau from uAgents to add the agents for checking and reporting the temperature
from uagents import Bureau

#Importing the agent for checking the current temperature
from agents.temp_check.temp_check import agent as temp_check

#Importing the agent for displaying if the temperature is 
#in the range set by the user
from agents.temp_receive.temp_receive import agent as temp_receive

# Defining the bureau
bureau = Bureau(endpoint="http://127.0.0.1:8000/submit", port=8000)

#Adding the imported agents to the bureau
bureau.add(temp_check)
bureau.add(temp_receive)

if __name__ == "__main__":
    bureau.run()