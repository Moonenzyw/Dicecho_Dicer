import random
from ..common.CommonFunc import *
from ..common.Message import *

from nonebot.plugin import require
from nonebot.adapters.cqhttp import Bot, Event
require_Card = require("dicer_with_card")

#暗骰
rhcmd = on_dicerCmd("rh", 2)
@rhcmd.handle()
async def rhhandle(bot: Bot, event: Event):
    pa = {}
    pa["name"] = require_Card.GetCardName(bot, event)
    pa["content"] = " " + str(event.get_message())[3:].strip() + ": " + r("d100")
    if IsGroupMessage(bot, event):
        res = await bot.get_group_info(group_id=groupid)
        pa["groupname"] = res["group_name"]
        pa["groupid"] = GetGroupId(bot, event)
        await bot.send_group_msg(group_id=event.group_id, message=FormatMessageByName("Hide_GroupMessage",pa))
        await bot.send_private_msg(user_id=uid, message=FormatMessageByName("Hide_Roll", pa))
    else:
        await rhcmd.finish(FormatMessageByName("Normal_Roll", pa))
