import asyncio
from TikTokLive import TikTokLiveClient
from telegram import Bot

TELEGRAM_TOKEN = "9172107020:AAHkGEzzvBQmZWf2fa9c4yrmNBtI1PruZyo"
TELEGRAM_CHAT_ID = "6531943722"

telegram_bot = Bot(token=TELEGRAM_TOKEN)

CREATORS = ["@ben.toye.lives", "@ekberows_her_yerde1"]

async def monitor_creator(username):
    client = TikTokLiveClient(unique_id=username)

    @client.on("connect")
    async def on_connect(event):
        print(f"🟢 Qoşuldu: {username}")
        await telegram_bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=f"🟢 Bot qoşuldu: {username} canlı yayımı yoxlanılır!")

    @client.on("gift")
    async def on_gift(event):
        if event.gift.streakable:
            msg = f"🎁 Sandıq/Hədiyyə tapıldı!\nYayım: {username}\nİstifadəçi: {event.user.nickname}\nHədiyyə: {event.gift.name}"
            print(msg)
            await telegram_bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=msg)

    try:
        await client.start()
    except Exception as e:
        print(f"{username} canlıda deyil: {e}")

async def main():
    while True:
        for creator in CREATORS:
            print(f"Yoxlanılır: {creator}")
            await monitor_creator(creator)
            await asyncio.sleep(5)

if __name__ == '__main__':
    asyncio.run(main())
  
