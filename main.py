from modules import *

config = _load_config()

api_id = config.get("API_ID")
if not api_id or str(api_id).lower() == "null":
    api_id = input("Set your Telegram API ID (https://my.telegram.org/auth): ")
    setAPI_ID(api_id)

api_hash = config.get("API_HASH")
if not api_hash or str(api_hash).lower() == "null":
    api_hash = input("Set your Telegram API Hash (https://my.telegram.org/auth): ")
    setAPI_HASH(api_hash)

client = initClient(api_id, api_hash)

async def main():
    await startClient(client)

    parentFolder = selectParentFolder()
    outputDir = initOutputDir(parentFolder)
    mediaDir = initMediaDir(outputDir)

    target = input("Set target channel (with @): ")     # Set target for current session

    messagesByDate = {}

    await export(client, target, messagesByDate, outputDir, mediaDir)
    save(outputDir, messagesByDate)

    print(f"✅ Successful export. {len(messagesByDate)} files created.")

with client:
    client.loop.run_until_complete(main())