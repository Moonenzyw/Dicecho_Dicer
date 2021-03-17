import random
import re
from ..common.CommonFunc import *
from ..common.Message import *
from .CardManager import *

from nonebot.adapters.cqhttp import Bot, Event
#ra
racmd = on_dicerCmd("ra", 2)
@racmd.handle()
async def rahandle(bot: Bot, event: Event):
    pa = {}
    pa["name"] = require_Card.GetCardName(bot, event)
    
    args = str(event.get_message())[3:].strip()
    anumstr = re.search("[0-9]*",args).group()
    anum = 0
    if len(anumstr)==0:
        anum = GetCardAttribute(bot, event, args)
    else:
        anum = int(anumstr)
    
    pa["content"] = ra(anum, args.replace(anumstr,""))
    await racmd.finish(FormatMessageByName("Check_Roll", pa))

def ra(anum : int, args : str):
    if anum < 0:
        return "人物卡未设置或没有对应属性！"
    
    rnd = random.randint(1,100)
    resend = ""

    if rnd == 100:
        resend = " 大失败"
    elif anum < 50 and rnd > 95:
        resend = " 大失败"
    elif rnd == 1:
        resend = " 大成功！"
    elif rnd <= anum // 5:
        resend = " 极难成功"
    elif rnd <= anum // 2:
        resend = " 困难成功"
    elif rnd <= anum:
        resend = " 成功"
    else:
        resend = " 失败"

    res = args + " : D100=" + str(rnd) + '/' + anum + resend
