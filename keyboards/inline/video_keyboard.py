from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def video_keyboards(link):
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
    return video
