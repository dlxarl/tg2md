from telethon import TelegramClient
import os

def initClient(api_id, api_hash):                               # Initialize client for Telegram API
    return TelegramClient('session_name', api_id, api_hash)

async def startClient(client):                               # Start client
    await client.start()

async def export(client, target, messagesByDate, outputDir, mediaDir):
    async for message in client.iter_messages(target):
        if not message.text and not message.media:
            continue

        date_str = message.date.strftime("%Y-%m-%d")
        time_str = message.date.strftime("%H:%M")

        if date_str not in messagesByDate:
            messagesByDate[date_str] = []

        entry_parts = [f"**{time_str}**"]

        # Text
        if message.text:
            entry_parts.append(message.text.strip())

        # Media
        if message.media:
            filename = f"{message.id}"
            path = await message.download_media(file=os.path.join(mediaDir, filename))
            if path:
                rel_path = os.path.relpath(path, outputDir)
                entry_parts.append(f"![]({rel_path})")

        messagesByDate[date_str].append(" — ".join(entry_parts))

def save(outputDir, messagesByDate):
    for date_str, msgs in messagesByDate.items():
        md_content = f"# {date_str}\n\n" + "\n\n---\n\n".join(msgs)
        with open(os.path.join(outputDir, f"{date_str}.md"), "w", encoding="utf-8") as f:
            f.write(md_content)