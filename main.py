import os
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# =========================
# CONFIG DARI RAILWAY VARIABLES
# =========================
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("SESSION_STRING")

TARGET_USERNAME = "SuntikMediaID"

client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)

# =========================
# AUTO REPLY (1 PESAN TETAP)
# =========================
FIXED_REPLY = "Halo 👋 Mau Order Suntik Sosmed? ke Sini Bang @SuntikMediaID"

# =========================
# AMBIL SEMUA GRUP
# =========================
async def get_all_groups():
    dialogs = await client.get_dialogs()
    return [d for d in dialogs if d.is_group or d.is_channel]

# =========================
# FORWARD KE SEMUA GRUP
# =========================
async def forward_to_groups(text, username):
    groups = await get_all_groups()

    print(f"📦 Total grup: {len(groups)}")

    for group in groups:
        try:
            await client.send_message(
                group.id,
                f"📩 Forward dari @{username}:\n\n{text}"
            )
        except:
            pass

# =========================
# EVENT HANDLER
# =========================
@client.on(events.NewMessage)
async def handler(event):
    try:
        sender = await event.get_sender()
        username = sender.username if sender else None
        text = event.raw_text

        # ✔ AUTO REPLY SEMUA CHAT
        await event.reply(FIXED_REPLY)

        # ✔ FILTER USER KHUSUS
        if username == TARGET_USERNAME:
            print("📢 Trigger dari @SuntikMediaID")
            await forward_to_groups(text, username)
            await asyncio.sleep(60)

    except Exception as e:
        print("Error:", e)

# =========================
# START BOT (FIX RAILWAY SAFE)
# =========================
async def main():
    print("🚀 Bot berjalan...")

    # ❗ ini penting: tidak akan minta login HP kalau session benar
    await client.connect()

    if not await client.is_user_authorized():
        print("❌ SESSION INVALID / KOSONG")
        return

    await client.run_until_disconnected()

client.loop.run_until_complete(main())
