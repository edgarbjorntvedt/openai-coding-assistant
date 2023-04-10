# OpenAI Code Improvement Tool

This script is designed to improve a given piece of JavaScript code using the OpenAI GPT-3 language model. This is a Python script that allows you to send your code to OpenAI to improve it using the OpenAI API. Your code should contain comments and other instructions that OpenAI will take into consideration while improving your code.

## How to use the tool

1.  Clone the repository or download the script file.
2.  Install the required packages by running `pip install -r requirements.txt`.
3.  Save you openai key (see section below).
3.  Find the path to your file to improve. Eg:`index.js`. If you want, you can include comments and instructions in your code.
4.  Run the Python script `improve_code.py` (see usage below)
5.  The improved code will be saved and you find a backup of your existing code named: `index.js.bck`.

## Usage

To run the script, simply call the Python interpreter with the script file as the argument:

`python3 improve_code.py --filename index.js --system-message-file system_message.txt`


## Output

The script will update your code and the original code will be backed up with a .bck suffix.

## OpenAI API key

To set the OpenAI API key from the command line, simply run:

`python3 config.py --key <your API key>`

You can also use the `--print` flag to display the current configuration:

`python3 config.py --print`

## Dependencies

-   Python 3.6 or later
-   `openai==0.10.2`
-   `python-dotenv==0.19.1`

## License

This tool is licensed under the MIT License. See the LICENSE file for more information.