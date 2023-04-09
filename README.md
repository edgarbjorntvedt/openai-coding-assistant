# OpenAI Code Improvement Tool

This is a Python script that allows you to send your code to OpenAI to improve it using the OpenAI API. Your code can contain comments and other instructions that OpenAI will take into consideration while improving your code.

## How to use the tool

1.  Create a `.env` file and add your OpenAI API configurations to the file. See `.env.sample` for an example of how the file should look.
2.  Install the required dependencies by running the following command in your terminal:


Copy code

`pip install -r requirements.txt`

3.  Add your code to a file named `index.mjs`. If you want, you can include comments and instructions in your code.
4.  Run the Python script `improve_code.py` by running the following command in your terminal:


Copy code

`python3 improve_code.py`

5.  The improved code will be saved in a file named `openai.index.mjs`.

## Configuration

You need to configure the tool with your OpenAI API keys and configurations. 
Add your API keys and configurations to a `.env` file that 
is located in the same directory as the Python script.

The following configurations need to be added to the `.env` file:

```
OPENAI_API_KEY=<your_api_key_here>
OPENAI_MODEL_ID=davinci-codex-001
INPUT_FILE=index.mjs
```

### OpenAI models
OpenAI offers two models for improving code:

-   `davinci-codex-001`: a newer model that analyzes and improves code for a wide range of programming languages.
-   `code-davinci-edit-001`: a highly accurate model for identifying and fixing common coding errors and inefficiencies. 
     This one is cheeper

To use these models for code improvement, integrate them into your development environment using OpenAI's API.

## Dependencies

-   Python 3.6 or later
-   `openai==0.10.2`
-   `python-dotenv==0.19.1`

## License
This tool is licensed under the MIT License. See the LICENSE file for more information.



