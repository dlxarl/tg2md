import json
import os

CONFIG_FILE = 'config.json'

def _load_config():                             # Load 'config.json'
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {}

def _save_config(config):                       # Save changes in 'config.json'
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)

def setAPI_ID(api_id):                          # Set Telegram API ID
    config = _load_config()
    config['API_ID'] = api_id
    _save_config(config)

def setAPI_HASH(api_hash):                      # Set Telegram API Hash
    config = _load_config()
    config['API_HASH'] = api_hash
    _save_config(config)