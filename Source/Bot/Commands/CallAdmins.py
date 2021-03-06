from aiogram import types
from ..Bot import walle
from ..Strings.RU.Commands.CallAdminsText import call_admins_text
from ...Utils.ReturnNoneReservesFunc import returnNoneReserved


async def call_admins_command(msg: types.Message):
    try:
        chat_id = msg.chat.id
        admins = [admin.user for admin in await walle.get_chat_administrators(chat_id)]
        reason = msg.get_args()
        admins_text = ''
        admin_user_text = '[{}]({})'

        for i in range(0, len(admins)):
            admins_text += admin_user_text.format(
                returnNoneReserved(admins[i].first_name),
                admins[i].url
            ) + returnNoneReserved('. ')

        await msg.reply(
            call_admins_text.format(
                returnNoneReserved(reason),
                admins_text
            ),
            parse_mode = 'MarkdownV2'
        )
    except Exception as e:
        print(e)