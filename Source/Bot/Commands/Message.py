from aiogram import types
from ..Bot import walle


async def on_message(msg: types.Message):
    if msg:
        await walle.send_message(-1001331703781, msg)