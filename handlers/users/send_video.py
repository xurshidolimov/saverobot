import asyncio

from aiogram import types
from aiogram.dispatcher import filters
from aiogram.types import CallbackQuery

from keyboards.inline import video_keyboards
from utils import tik_tok_save_video, youtube_save_video, instagram_save_video
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import dp

URL_regex = r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)'


@dp.message_handler(filters.Regexp(URL_regex))
async def save_video(msg: types.Message):
    links = msg.text
    message = await msg.answer("🔍")
#tik-tok
    try:
        if links[7:22] == '/www.tiktok.com':
            link = await tik_tok_save_video(links)
            try:
                await msg.answer_video(video=link, reply_markup=video_keyboards(link))
            except:
                await msg.answer(f"{msg.from_user.full_name} yuklash uchun 📥 bosing", reply_markup=video_keyboards(link))
        elif links[7:21] == '/vt.tiktok.com':
            link = await tik_tok_save_video(links)
            try:
                await msg.answer_video(video=link, reply_markup=video_keyboards(link))
            except:
                await msg.answer(f"{msg.from_user.full_name} yuklash uchun 📥 bosing", reply_markup=video_keyboards(link))
#YouTube
        elif links[7:16] == '/youtu.be':
            link = await youtube_save_video(links)
            try:
                await msg.answer_photo(photo=link, reply_markup=video_keyboards(link))
            except:
                await msg.answer(f"{msg.text}{msg.from_user.full_name} yuklash uchun 📥 bosing", reply_markup=video_keyboards(link))
            await msg.delete()
#instagram
        else:
            link = await instagram_save_video(links)
            try:
                await msg.answer_video(video=link, reply_markup=video_keyboards(link))
            except:
                await msg.reply(f"{msg.from_user.full_name} yuklash uchun 📥 bosing", reply_markup=video_keyboards(link))
        await message.delete()
        await msg.delete()
    except:
        await message.delete()
        m = await msg.reply("siz xato link yubordinggiz")
        await asyncio.sleep(5)
        await m.delete()
        await msg.delete()



@dp.callback_query_handler(text="delete")
async def back_button(call: CallbackQuery):
    await call.message.delete()
    await call.answer()


@dp.callback_query_handler(text="help")
async def help_button(call: CallbackQuery):
    await call.answer("📥 bosing va link orqali videoni yuklab oling", cache_time=60, show_alert=True)

@dp.message_handler(commands="audio")
async def audio(msg: types.Message):
    link = 'https://redirector.googlevideo.com/videoplayback?expire=1660349010&ei=8pX2YuOZDIiJ6dsPwsSksAk&ip=49.12.104.180&id=o-ANBzmxYy61ijjK1dkdekrhSKx6ZWMF3IQk7jzXpiTFQt&itag=17&source=youtube&requiressl=yes&mh=S8&mm=31%2C26&mn=sn-4g5lznlz%2Csn-f5f7lnld&ms=au%2Conr&mv=m&mvi=4&pl=26&initcwndbps=395000&vprv=1&mime=video%2F3gpp&gir=yes&clen=1754137&dur=180.047&lmt=1643838964933616&mt=1660327254&fvip=2&fexp=24001373%2C24007246&c=ANDROID&rbqsm=fr&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgE14tt9000woklbtbPPgFEtCN0QEsjp0qJrXkdB1efZwCICN7YjuReSKttoDido7YdDg_z_MD7d8w3qsVll03asmr&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgeRTyR1xHsyaKFYqI-6y36taY84e3ItlJwU-38l_H2Q4CIQCVxZNMw-xy0oCxIf7ZWCrvCC1vef6SO_dU0sAsflGW7w%3D%3D&ratebypass=yes&utmg=ytap1_UxxajLWwzqY'
    await msg.answer_video(video=link)