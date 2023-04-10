import argparse
import os
import json
import requests

parser = argparse.ArgumentParser(description='Improve code using OpenAI GPT-3')
parser.add_argument('--filename', type=str, help='Filename of the code to be improved', required=True)
parser.add_argument('--key', type=str, help='API key for OpenAI', required=True)
parser.add_argument('--system-message-file', type=str, help='Filename of the system message', required=True)
args = parser.parse_args()

with open(args.filename) as f:
    code = f.read()

with open(args.system_message_file) as f:
    system_message = f.read().strip()

token_length = int(len(code + ' ' + system_message) * 1.1 / 4)
print(f"guessed token_length: {token_length}")

response = requests.post(
    'https://api.openai.com/v1/chat/completions',
    headers={
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {args.key}',
    },
    json={
        'model': 'gpt-3.5-turbo',
        'messages': [
            {'role': 'system', 'content': system_message},
            {'role': 'user', 'content': code},
        ],
        'temperature': 0.2,
        'max_tokens': 4097 - token_length,
    }
)

response_json = response.json()

new_response = json.loads(json.dumps(response_json))
for choice in new_response['choices']:
    choice['message']['content'] = '...'
print(json.dumps(new_response, indent=2))

improved_code = response_json["choices"][0]["message"]["content"]

os.rename(args.filename, f'{args.filename}.bck')

with open(args.filename, 'w') as f:
    f.write(improved_code)
