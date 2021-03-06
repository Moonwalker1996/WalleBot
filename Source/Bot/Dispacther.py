from aiogram import Dispatcher
from .Bot import walle


# Importing bot commands
from .Commands.Start import start_command
from .Commands.Cmds import cmds_command
from .Commands.NewMembers import new_group_user
from .Commands.LeftChatMember import left_group_user
from .Commands.Stat import stat_command
from .Commands.RemoveSystemMessages import remove_system_msg
from .Commands.Mute import mute_command
from .Commands.Unmute import unmute_command
from .Commands.Ban import ban_command
from .Commands.Unban import unban_command
from .Commands.Pin import pin_command
from .Commands.ActionsFilter import actions_filter
from .Commands.Antiflood import antiflood
from .Commands.CallAdmins import call_admins_command
from .Commands.DuelGame.NewDuel import duel_command
from .Commands.Weather import weather_command

dp = Dispatcher(walle)


# Default
dp.register_message_handler(cmds_command, commands = ['cmds'])
dp.register_message_handler(start_command, commands = ['start'])
dp.register_message_handler(stat_command, commands = ['stat'])
dp.register_message_handler(call_admins_command, commands = ['call_adms'])
dp.register_message_handler(weather_command, commands = ['weather'])
dp.register_message_handler(duel_command, commands = ['duel'])


# Moderation
dp.register_message_handler(mute_command, commands = ['mute'], commands_prefix = '*')
dp.register_message_handler(unmute_command, commands = ['unmute'], commands_prefix = '*')
dp.register_message_handler(ban_command, commands = ['ban'], commands_prefix = '*')
dp.register_message_handler(unban_command, commands = ['unban'], commands_prefix = '*')
dp.register_message_handler(pin_command, commands = ['pin'], commands_prefix = '*')


# Events
dp.register_message_handler(new_group_user, content_types = ['new_chat_members'])
dp.register_message_handler(left_group_user, content_types = ['left_chat_member'])
dp.register_message_handler(dp.async_task(remove_system_msg), content_types = ['pinned_message'])
dp.register_message_handler(dp.async_task(actions_filter), content_types = ['text'])
#dp.register_message_handler(dp.async_task(antiflood), content_types = ['any', 'text'])
#dp.register_callback_query_handler(duel_callb_listener, lambda callb_query: True)
