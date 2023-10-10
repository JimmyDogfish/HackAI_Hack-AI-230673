# Code reference for obtaining temperature using OpenWeatherAPI taken from 
# https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/ article written by ankthon
# Code reference for creating agents taken from uAgent documentation and 
# YouTube Channel provided in the Problem Statement

# import required modules for fetching the data and creating agents
import requests, json
from uagents import Agent, Context, Model
from uagents.setup import fund_agent_if_low

#Importing the temp_receive agent to get its address
#The current temperature will be sent to this agent
#For it to display it on the console
from agents.temp_receive.temp_receive import agent as temp_receive

# Enter your API key here. Detailed instructions for creating it can be found in the README.md
api_key = "Api_Key"

# base_url variable to store url from open weather map
base_url = "http://api.openweathermap.org/data/2.5/weather?"
 
# Give city name
city_name = input("Enter city name : ")

# complete url address to receive the temperature for the selected city
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
 
# get method of requests module and return response object
response = requests.get(complete_url)

#storing and converting the response in a variable
x = response.json()

#Check if the value of cod is equal to 404
#That means the city entered is invalid
# So end the program

if x["cod"] == "404":
    print(" City Not Found ")
    exit()

# Define the class Message to send and receive message between agents
class Message(Model):
    message: str;

#Defining the address of temp_receive agent
RECIPIENT_ADDRESS = temp_receive.address

#Defining the agent to check the temperature
agent = Agent(name="temp_check", seed="temperature recovery phrase")

#Funding the agent to remove the error 'Agent does not have enough funds'
fund_agent_if_low(agent.wallet.address())

# store the value of "main" key in variable y
y = x["main"]

# store the value corresponding to the "temp" key of y and
#  convert it to celsius from kelvin
current_temperature = int(y["temp"]-273.5,)

#Take the maximum and minimum temperature from the user
max_temp = input("Enter your maximum temperature: ")
min_temp = input("Enter your minimum temperature: ")
max_temp = int(max_temp)
min_temp = int(min_temp)

# setting up the agent to access the real time temperature 
# after a interval of 90 seconds. This can be changed by chaining the 
# period value to desired value (in seconds)
#The agent checks if the temperature is beyond the limits or not
#and sends the message to temp_receive agent

@agent.on_interval(period=90.0)
async def temperature_check(ctx: Context):
    if max_temp < current_temperature:
        await ctx.send(RECIPIENT_ADDRESS, Message(message=f"\033[1;31;40m The current temperature exceeds the maximum temperature ({max_temp})°C by {current_temperature-max_temp}°C"))
    elif min_temp > current_temperature:
        await ctx.send(RECIPIENT_ADDRESS, Message(message=f"\033[1;31;40m The current temperature is lower than the minimum temperature ({min_temp})°C by {min_temp-current_temperature}°C"))
    else:
        await ctx.send(RECIPIENT_ADDRESS, Message(message=f"\033[1;32m The current temperature is in the range set by you {min_temp}°C-{max_temp}°C"))   