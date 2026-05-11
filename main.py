from telethon import TelegramClient, events
import os

api_id = int(os.getenv("39944653"))
api_hash = os.getenv("22a3ee5dbe3a627f8f7c78fcbc8eb995")
session = os.getenv("1BVtsOLEBu4FAR5Qu5lcu4liHXkWu8pkdiXeswx1av9EYjK_Xorad2b3d3YKT4ow8a9nSieOAXgGngzxC2DZvEnrhRPByVjHYfZLULcC0zX5KnUS4416wd2UFPZu9Y_WNMppo7k-3o4HNZ8xKebD0M0tA85XI0-fq0z21P-ahnDu079Y9JRhRDGP_IPfxL47bHpH9lFsdJFhFbt-yv8-Yte2BrmpLxamX2JeVi0HgKXtseoZxSxdCoOL9OitRenvjER5q78Txh3XC53zoa-CBVpWwUSn0HJuFci5J8LWsK5jok7u6WdvNkCxVjnyWD5wV8CADLiyrgjBq2NAHI5eThHFuuYp29Po=")

client = TelegramClient(session, api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if event.is_private:
        await event.reply("Halo 👋 Mau Order Suntik Sosmed? ke Sini Bang @SuntikMediaID.")

print("Bot running...")
client.start()
client.run_until_disconnected()
