from aiogram import types
from ...Bot import walle


public_tablet = []
activity_tablet = []


async def adms_activity(msg: types.Message):
    print(activity_tablet)
    print(public_tablet)
    await refresh_tablet(message = msg)
    await msg.answer(public_tablet)


async def refresh_tablet(message: types.Message):
    try:
        chat_id = message.chat.id
        admins = [admin.user for admin in await walle.get_chat_administrators(chat_id)]

        for adm in admins:
            if adm in activity_tablet:
                pass
            else:
                activity_tablet.append("{}:Online".format(adm))
                public_tablet.append("{}:Online".format(adm.first_name))
    except Exception as e:
        print(e)


def makeOnline(text: str):
    if 'Offline' in text:
        return text.replace('Offline', 'Online')
    
def makeOffline(text: str):
    if 'Online' in text:
        return text.replace('Online', 'Offline')
    