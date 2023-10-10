# Hack AI Submission
This repository contains the submission for Hack AI conducted by IITB Techfest and fetch.ai 
### Team ID - Hack AI-230673
### Team Members - Apoorva Jha, Satyam Parsai, Anush Sharma, Akshit Amit Bilgaiyan

## Instructions for running and using the program
For obtaining the API from OpenWeather Map us this link - https://openweathermap.org/api  
You will have to register to get the API key  
Once registered, you will be able to find your key under 'API Key' tab in the OpenWeather dashboard  
Once obtained, navigate to ``` hack-ai/src/agents/temp_check/temp_check.py ``` and change ``` api_key = "Api_Key" ``` to the API key you obtained

Then, to run the program, navigate to the hack-ai folder and use the following commands  
Note - poetry must be installed and python version must be between >=3.8 and <3.12  


``` 
poetry shell
poetry install 
python /src/main.py 
```

Then enter your city and max and min temperature  
The program will monitor the temperature every 90 seconds and alert you if to goes out of the range

Thanks!
