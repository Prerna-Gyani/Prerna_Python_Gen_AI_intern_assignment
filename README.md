# Prerna_Python_Gen_AI_intern_assignment
Assignment completed: API endpoint: https://devapi.beyondchats.com/api/get_message_with_sources
Above is a paginated GET API which returns an array of objects where each object contains a response text and a corresponding array of sources. 
source is a JSON array. Each object of the array consists of an id, context, and an optional link.

Your task is to develop a Python program that does the following:

Fetch the data from the pages of the API above.
Identify whether the response for each response-sources pair came from any of the sources
List down the sources from which the response was formed. Returns an empty array if the response did not come from any source. The shortlisted sources will be called citations
Return the citations for all objects coming from the API. 
Extra points if you can present your solution through a user-friendly UI.


Technologies to Use:
Feel free to use any tools or libraries in Python needed to accomplish this task. The use of LLMs, NLP, ML/AI is encouraged.
# Given code checked according to sample input & output given in 
https://docs.google.com/document/d/1u5HOIw_asgWVWjdK-FiNJbu1SlVhCkJWzYNN9IfO5qM/edit

## Requirements:
tkinter and pip

## Description of execution
# Code: Provided in newinter.py file
# To run file: open python idle or any other python editor
# Click run or f5
<img width="391" alt="image" src="https://github.com/Prerna-Gyani/Prerna_Python_Gen_AI_intern_assignment/assets/142766837/72a58d32-cb8d-4968-8ba5-35112b1dd268">

# On python shell tkinter window opens --> Click Fetch Data
![image](https://github.com/Prerna-Gyani/Prerna_Python_Gen_AI_intern_assignment/assets/142766837/e0f92d4d-3d06-4114-96be-cf4503f3d941)

# On console cmd python shell output will be generated
![image](https://github.com/Prerna-Gyani/Prerna_Python_Gen_AI_intern_assignment/assets/142766837/8a9417f8-2e04-4d09-8e38-900c9a15ebf9)

