import asyncio
from time import time
from datetime import datetime
from config import BOT_USERNAME, UPDATES_CHANNEL, ZAID_SUPPORT
from helpers.filters import command
from helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/899cf677d90a10b907a15.png",
        caption=f"""**@Yasakakrallik icin özel yapılmış Muzin Botudur olası durumlarda Muzik Asistanını Elle Eklemeniz Gerekebilir Keyifli Muzik Dinlemeler ...
💞 Asistana Burdan Ulaşabilirsiniz 
[Asistan Player](t.me/TubidyMusicAsistanPlayer) ...
**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ BENİ GRUBA EKLE ❱ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "YARDIM VE KOMUTLAR", url=f"https://t.me/SUPERIOR_BOTS/160"
                    ),
                    InlineKeyboardButton(
                        "SAHİP", url="https://t.me/Dnztrmn"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📢 RESMİ KANAL", url=f"https://t.me/yalnzadmlr"
                    ),
                    InlineKeyboardButton(
                        "RESMİ GRUP 🇹🇷", url="https://t.me/YasakKrallik"
                    )
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/a45bd27a16f92285120c8.png",
        caption=f"""EKLEDİĞİN İÇİN TEŞEKKÜRLER 🔥♥️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 YARDIM VE KOMUTLAR 💞", url=f"https://t.me/tubidybotdestek")
                ]
            ]
        ),
    )


@Client.on_message(command(["repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/4c098ec0d9fb56a89f3c7.png",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 SOHBET GRUBUNA GİTMEK İCİN TIKLA 💞", url=f"https://t.me/Dnztrmn")
                ]
            ]
        ),
    )
