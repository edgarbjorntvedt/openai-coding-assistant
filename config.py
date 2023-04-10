import argparse
import os
import json
import sys

sys.path.append(os.path.abspath('./lib'))
import config_helper

parser = argparse.ArgumentParser(description='Set OpenAI API key')
parser.add_argument('--key', type=str, help='API key for OpenAI')
parser.add_argument('--print', action='store_true', help='Print the current API key')
args = parser.parse_args()

if args.print:
    print(f"Current API key: {config_helper.get_api_key()}")
elif args.key:
    config_helper.save_api_key(args.key)
    print(f"API key set to: {args.key}")
else:
    print("No command specified. Use --key to set an API key or --print to print the current API key.")