from aiogram import types
from aiogram.dispatcher import filters
from aiogram.types import CallbackQuery

from loader import dp
from keyboards.inline.save_video_keyboard import video_keyboard

URL_regex = r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)'


@dp.message_handler(filters.Regexp(URL_regex))
async def save_video(msg: types.Message):
        return video_keyboard(msg)


@dp.callback_query_handler(text="delete")
async def back_button(call: CallbackQuery):
    await call.message.delete()
    await call.message.reply_to_message.delete()
    await call.answer()


@dp.callback_query_handler(text="help")
async def help_button(call: CallbackQuery):
    await call.answer("📥 bosing va link orqali videoni yuklab oling", cache_time=60, show_alert=True)

