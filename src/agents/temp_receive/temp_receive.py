# Code reference for creating agents taken from uAgent documentation 
# and YouTube Channel provided in the Problem Statement

#Import required modules from uAgent
from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low

# Define class message to receive message from temp_check agent
class Message(Model):
    message: str;

# Creating the agent temp_receive to receive the messages from temp_check agent
agent = Agent(name='temp_receive', seed='temp_receive recovery phrase')
fund_agent_if_low(agent.wallet.address())
#Defining the behavior for the agent
#It receives messages from temp_check and logs them to the console
@agent.on_message(model=Message)
async def temp_check_message_handler(ctx:Context, sender:str, msg:Message):
    ctx.logger.info(f'{msg.message}')