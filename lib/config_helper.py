import os
import configparser

config_folder = os.path.join(os.path.expanduser("~"), ".openai")
if not os.path.exists(config_folder):
    os.makedirs(config_folder)

config_file = os.path.join(config_folder, ".config")

config = configparser.ConfigParser()
if os.path.exists(config_file):
    config.read(config_file)

if not 'DEFAULT' in config:
    config['DEFAULT'] = {}

if not 'api_key' in config['DEFAULT']:
    config['DEFAULT']['api_key'] = 'YOUR_API_KEY_HERE'
    with open(config_file, 'w') as f:
        config.write(f)

def get_api_key():
    config.read(config_file)
    return config['DEFAULT']['api_key']

def save_api_key(key):
    config.read(config_file)
    config['DEFAULT']['api_key'] = key
    with open(config_file, 'w') as f:
        config.write(f)
