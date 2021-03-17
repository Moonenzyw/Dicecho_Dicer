from .data_source import Do_Dice, help_message, st, en
from .madness import ti, li
from .create import Investigator
from .san_check import sc
from .messages import *

from nonebot.plugin import on_startswith
from nonebot.adapters.cqhttp import Bot, Event

rdhelp = on_startswith(".help", priority=2)
stcommand = on_startswith(".st", priority=2)
encommand = on_startswith(".en", priority=2)
licommand = on_startswith(".li", priority=2)
coc = on_startswith(".coc", priority=2)
sccommand = on_startswith(".sc", priority=2)
rdcommand = on_startswith(".r", priority=3)


@rdhelp.handle()
async def rdhelphandler(bot: Bot):
    await rdhelp.finish(help_message())


@stcommand.handle()
async def stcommandhandler(bot: Bot):
    await rdhelp.finish(st())


@encommand.handle()
async def enhandler(bot: Bot, event: Event):
    args = str(event.get_message())[3:].strip()
    await encommand.finish(en(args))


@rdcommand.handle()
async def rdcommandhandler(bot: Bot, event: Event):
    args = str(event.get_message())[2:].strip()
    uid = event.get_session_id()
    if args and not("." in args):
        groupid = event.group_id if event.get_event_name().startswith("message.group") else 0
        groupname = ""
        if groupid != 0:
            res = await bot.get_group_info(group_id=groupid)
            groupname = res["group_name"]

        isHide, rrd = Do_Dice(args, event.sender.nickname, groupid, str(groupname))
        if not isHide:
            await rdcommand.finish(rrd)
        else:
            await bot.send_group_msg(group_id=event.group_id, message=FormatMessageByName("Hide_GroupMessage",{"name" : event.sender.nickname}))
            await bot.send_private_msg(user_id=uid, message=rrd)


@coc.handle()
async def cochandler(bot: Bot, event: Event):
    args = str(event.get_message())[4:].strip()
    try:
        args = int(args)
    except:
        args = 20
    inv = Investigator()
    inv.age_change(args)
    await coc.finish(inv.output())

@licommand.handle()
async def licommandhandler(bot: Bot):
    await licommand.finish(li())


@sccommand.handle()
async def schandler(bot: Bot, event: Event):
    args = str(event.get_message())[3:].strip()
    await sccommand.finish(sc(args.lower()))
