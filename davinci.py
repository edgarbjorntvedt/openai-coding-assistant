import requests
import json
from dotenv import dotenv_values

# Load the OpenAI API key and other configurations from the .env file
config = dotenv_values(".env")
api_key = config["OPENAI_API_KEY"]
filename = config["FILENAME"]

# Load the content of the file index.mjs
with open(filename, "r") as file:
    code = file.read()

# Set up the API endpoint URL
url = "https://api.openai.com/v1/edits"

# Set up the request headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
}

# Set up the request data
data = {
    "model": "text-davinci-edit-001",
    "input": code,
#     "instruction": "You are a Javascript help with code improvments. You receive a file with working code. Your job is to improve the code based on the comments in the file. Your output must be working code as well",
    "instruction": "You are a Javascript help with code improvements. You receive a file with working code. Your job is to improve the code based on the comments in the file. Your output must be working code as well",
    "temperature": 0.5
}

# Send the request to the API
response = requests.post(url, headers=headers, data=json.dumps(data))

# Parse the response JSON
response_json = json.loads(response.text)

print(response_json)

# Extract the generated text from the response
improved_code = response_json["choices"][0]["text"]

# Write the improved code to the file openai.index.mjs
with open("openai." + filename, "w") as file:
    file.write(improved_code)
