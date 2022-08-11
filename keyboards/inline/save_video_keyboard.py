import asyncio

from aiogram.dispatcher import filters
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
from loader import dp
from utils import tik_tok_save_video, youtube_save_video, instagram_save_video
URL_regex = r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)'


@dp.message_handler(filters.Regexp(URL_regex))
async def video_keyboard(msg: types.Message):
    links = msg.text
    try:
        if links[7:22] == '/www.tiktok.com':
            link = await tik_tok_save_video(msg.text)
            try:
                video = InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            InlineKeyboardButton(text="📥", url=link)
                        ],
                        [
                            InlineKeyboardButton(text="🆘", callback_data="help"),
                            InlineKeyboardButton(text="❌", callback_data="delete")
                        ]
                    ]
                )
                await msg.reply_video(video=link, reply_markup=video)
            except:
                video = InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            InlineKeyboardButton(text="📥save", url=link)
                        ],
                        [
                            InlineKeyboardButton(text="🆘", callback_data="help"),
                            InlineKeyboardButton(text="❌", callback_data="delete")
                        ]
                    ]
                )
                await msg.reply(f'{msg.from_user.full_name} tugmani bosing', reply_markup=video)
        elif links[7:21] == '/vt.tiktok.com':
            link = await tik_tok_save_video(msg.text)
            try:
                video = InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            InlineKeyboardButton(text="📥", url=link)
                        ],
                        [
                            InlineKeyboardButton(text="🆘", callback_data="help"),
                            InlineKeyboardButton(text="❌", callback_data="delete")
                        ]
                    ]
                )
                await msg.reply_video(video=link, reply_markup=video)
            except:
                video = InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            InlineKeyboardButton(text="📥save", url=link)
                        ],
                        [
                            InlineKeyboardButton(text="🆘", callback_data="help"),
                            InlineKeyboardButton(text="❌", callback_data="delete")
                        ]
                    ]
                )
                await msg.reply(f'{msg.from_user.full_name} tugmani bosing', reply_markup=video)
        elif links[7:16] == '/youtu.be':
            link = await youtube_save_video(msg.text)
            try:
                video = InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            InlineKeyboardButton(text="📥", url=link)
                        ],
                        [
                            InlineKeyboardButton(text="🆘", callback_data="help"),
                            InlineKeyboardButton(text="❌", callback_data="delete")
                        ]
                    ]
                )
                await msg.reply_video(video=link, reply_markup=video)
            except:
                video = InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            InlineKeyboardButton(text="📥", url=link)
                        ],
                        [
                            InlineKeyboardButton(text="🆘", callback_data="help"),
                            InlineKeyboardButton(text="❌", callback_data="delete")
                        ]
                    ]
                )
                await msg.reply(f'{msg.from_user.full_name} tugmani bosing', reply_markup=video)
        else:
            link = await instagram_save_video(msg.text)
            try:
                video = InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            InlineKeyboardButton(text="📥", url=link)
                        ],
                        [
                            InlineKeyboardButton(text="🆘", callback_data="help"),
                            InlineKeyboardButton(text="❌", callback_data="delete")
                        ]
                    ]
                )
                await msg.reply_video(video=link, reply_markup=video)
            except:
                video = InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            InlineKeyboardButton(text="📥", url=link)
                        ],
                        [
                            InlineKeyboardButton(text="🆘", callback_data="help"),
                            InlineKeyboardButton(text="❌", callback_data="delete")
                        ]
                    ]
                )
                await msg.reply(f'{msg.from_user.full_name} tugmani bosing', reply_markup=video)
    except:
        response = await msg.reply('siz hato link yubordinggiz')
        await asyncio.sleep(8)
        await response.delete()
        await msg.delete()
