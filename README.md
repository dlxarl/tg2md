# tg2md

A simple Python tool to export messages from Telegram to Markdown format.

## Features
- Connects to Telegram via Telethon
- Exports chat messages to Markdown
- Easy configuration via `config.json`

## Requirements
- Python 3.8+
- [Telethon](https://github.com/LonamiWebs/Telethon)

## Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/dlxarl/tg2md.git
   cd tg2md
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up your Telegram API credentials:
   - Run the script. On first launch, you will be prompted for your API ID and API Hash (get them at https://my.telegram.org/auth).
   - Credentials are saved in `config.json` (which is in .gitignore).

## Usage
Run the main script:
```sh
python main.py
```
Follow the prompts to authenticate and export messages.

## Notes
- Do not share your API credentials or session files.
