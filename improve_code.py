import openai
from dotenv import dotenv_values

# Load the OpenAI API key and other configurations from the .env file
config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]
model = config["OPENAI_MODEL"]
filename = config["FILENAME"]

# Load the content of the file index.mjs
with open(filename, "r") as file:
    code = file.read()

# Send the code to OpenAI for code improvements
response = openai.Completion.create(
#     model=model,
    engine=model,
    prompt=code,
    max_tokens=100,
    n=1,
    stop=None,
    temperature=0.7,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

# Extract the improved code from the OpenAI response
improved_code = response.choices[0].text

# Write the improved code to the file openai.index.mjs
with open("openai." + filename, "w") as file:
    file.write(improved_code)
