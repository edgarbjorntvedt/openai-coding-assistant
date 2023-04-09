import openai
from dotenv import dotenv_values

# Load the OpenAI API key and other configurations from the .env file
config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

# Get the list of engines
engines = openai.Engine.list()

# Print the id of each engine
for engine in engines['data']:
    print(engine['id'])