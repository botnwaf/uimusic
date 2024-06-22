
import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","‹ السورس ›"," ","السورس"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/e1e150db1fb721e7e6938.jpg",
        caption = f"""<b>  𝒘𝒆𝒍𝒄𝒐𝒎𝒆𝒖 𝒕𝒐 <b>\n<a href="https://t.me/ngd_1"> 𝒔𝒐𝒖𝒓𝒄𝒆 𝒄𝒎</a></b>""",
reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "  𝒅𝒆𝒗 ", url=f"https://t.me/a_re_a"),
                ],[
                    
                
                    InlineKeyboardButton(
                        " 𝒔𝒐𝒖𝒓𝒄𝒆 𝒄𝒎", url=f"https://t.me/a_re_aa"),         
                ],

            ]

        ),

)
