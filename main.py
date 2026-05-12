import os
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# =========================
# CONFIG
# =========================
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("SESSION_STRING")

TARGET_USERNAME = "SuntikMediaID"

client = TelegramClient(
    StringSession(SESSION),
    API_ID,
    API_HASH
)

# =========================
# AUTO REPLY
# =========================
FIXED_REPLY = "Halo 👋 Mau Order Suntik Sosmed? ke Sini Bang @SuntikMediaID"

# =========================
# AMBIL SEMUA GRUP
# =========================
async def get_all_groups():
    dialogs = await client.get_dialogs()
    groups = []

    for d in dialogs:
        if d.is_group:
            groups.append(d)

    return groups

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

            print(f"✅ Terkirim ke: {group.name}")

            # DELAY 1 MENIT
            await asyncio.sleep(60)

        except Exception as e:
            print(f"❌ Gagal ke {group.name}: {e}")

# =========================
# EVENT CHAT MASUK
# =========================
@client.on(events.NewMessage(incoming=True))
async def handler(event):

    # ❌ jangan balas grup/channel
    if event.is_group or event.is_channel:
        return

    try:
        sender = await event.get_sender()

        if not sender:
            return

        username = sender.username
        text = event.raw_text

        # =========================
        # AUTO REPLY CHAT PRIVATE
        # =========================
        await event.reply(FIXED_REPLY)

        # =========================
        # FORWARD USER TERTENTU
        # =========================
        if username and username.lower() == TARGET_USERNAME.lower():

            print(f"📢 Trigger dari @{username}")

            await forward_to_groups(text, username)

    except Exception as e:
        print("❌ Error:", e)

# =========================
# MAIN
# =========================
async def main():

    print("🚀 Bot berjalan...")

    await client.connect()

    if not await client.is_user_authorized():
        print("❌ SESSION INVALID / KOSONG")
        return

    me = await client.get_me()

    print(f"✅ Login sebagai: {me.first_name}")

    await client.run_until_disconnected()

asyncio.run(main())
