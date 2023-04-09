import requests
import json
from dotenv import dotenv_values

# Load the OpenAI API key and other configurations from the .env file
config = dotenv_values(".env")
api_key = config["OPENAI_API_KEY"]
filename = sys.argv[1] if len(sys.argv) > 1 else config["FILENAME"]
system_message_file = config["SYSTEM_MESSAGE_FILE"]

# Load the content of the file index.mjs
with open(filename, "r") as file:
    code = file.read()

# Set up the API endpoint URL
url = "https://api.openai.com/v1/chat/completions"

# Set up the request headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
}
# Load the content of the system message file
with open(system_message_file, 'r') as f:
    system_message = f.read().strip()

token_length = int(len(code + ' ' + system_message)*1.1/4)
print("guessed token_length: ", token_length)

# Set up the request data
data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": "system",
            "content": system_message
        },
        {
            "role": "user",
            "content":code
        },
        ],
    "temperature": 0.2,
    "max_tokens": 4097 - token_length,
}

# Send the request to the API
response = requests.post(url, headers=headers, data=json.dumps(data))

# Parse the response JSON
response_json = json.loads(response.text)

# deep copy the response
new_response = json.loads(json.dumps(response_json))
# remove the content field from each message
for choice in new_response['choices']:
    choice['message']['content'] = '...'

# print the modified response
print(json.dumps(new_response, indent=2))

# Extract the generated text from the response
improved_code = response_json["choices"][0]["message"]["content"]

# Backup the original file
os.rename(filename, filename + ".bck")

# Write the improved code to the file with the same filename as the original file
with open(filename, "w") as file:
    file.write(improved_code)
