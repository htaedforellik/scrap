import csv
from telethon import *
import python_socks
from resorse import *
import asyncio
import csv

tclient = TelegramClient('anon', api_id, api_hash )

csv_file = 'telegram_messages.csv'


async def main():
    await tclient.start()
    offset_id = 0
    limit = 10
    while True:
        messages = await tclient.get_messages("AWHTarchive", limit=limit, offset_id=offset_id)
        if not messages:
            break
        for message in messages:
            if message.document is not None:
                for attribute in message.document.attributes:
                    if isinstance(attribute, types.DocumentAttributeFilename):
                        file_name = attribute.file_name
                        message_link = f"https://t.me/AWHTarchive/{message.id}"
                        with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
                            writer = csv.writer(file)
                            writer.writerow([file_name, message_link])
                            print("اطلاعات به فایل CSV اضافه شد.")
        offset_id = messages[-1].id
        await asyncio.sleep(60)  # تاخیر یک دقیقه
    await tclient.run_until_disconnected()

asyncio.run(main())
