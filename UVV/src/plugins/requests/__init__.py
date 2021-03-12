#用于处理加好友、加群等信息
from nonebot.plugin import *
from nonebot.adapters.cqhttp import Bot, Event

requestCmd = on_request(priority=5)

@requestCmd.handle()
async def requesthandle(bot: Bot, event: Event):
    #TODO 黑名单
    await event.approve(bot)
