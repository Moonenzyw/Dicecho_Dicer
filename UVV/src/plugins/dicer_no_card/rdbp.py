from .rXdY import r

from nonebot.plugin import require
from nonebot.adapters.cqhttp import Bot, Event

import random

require_Card = require("dicer_with_card")

#rd
rdcmd = on_dicerCmd("rd", 2)
@rdcmd.handle()
async def rdhandle(bot: Bot, event: Event):
    args = str(event.get_message())[3:].strip()
    pa = {}
    pa["name"] = require_Card.GetCardName(bot,event)
    pa["content"] = r("d100" + args)
    await rdcmd.finish(FormatMessageByName("Normal_Roll", pa))

#rp
rpcmd = on_dicerCmd("rp", 2)
@rpcmd.handle()
async def rphandle(bot: Bot, event: Event):
    args = str(event.get_message())[3:].strip()
    pa = {}
    pa["name"] = require_Card.GetCardName(bot,event)
    pa["content"] = rp(args)
    await rpcmd.finish(FormatMessageByName("Normal_Roll", pa))

def rp(args):
    pnum = re.match("[0-9]*",args).group()
    num = 1
    if len(pnum) >= 0:
        num = int(pnum)
    if num >= 10:
        return "惩罚骰数过多。"

    args = args.replace(pnum,"")
    normal = random.randint(1,100)
    normala = normal // 10 #十位
    normalb = normal % 10 #个位
    res = args + " : P" + str(num) + "=" + str(normala * 10 + normalb) + "[惩罚骰:"
    for i in range(0,num):
        rnd = random.randint(0,9)
        res += ' ' + str(rnd)
        normala = max(normala, rnd)
    res += "]=" + str(normala * 10 + normalb)
    return res

#rb
rbcmd = on_dicerCmd("rb", 2)
@rbcmd.handle()
async def rbhandle(bot: Bot, event: Event):
    args = str(event.get_message())[3:].strip()
    pa = {}
    pa["name"] = require_Card.GetCardName(bot,event)
    pa["content"] = rb(args)
    await rbcmd.finish(FormatMessageByName("Normal_Roll", pa))

def rb(args):
    pnum = re.match("[0-9]*",args).group()
    num = 1
    if len(pnum) >= 0:
        num = int(pnum)
    if num >= 10:
        return "奖励骰数过多。"

    args = args.replace(pnum,"")
    normala = random.randint(0,9) #十位
    normalb = random.randint(1,10) #个位
    res = args + " : B" + str(num) + "=" + str(normala * 10 + normalb) + "[奖励骰:"
    for i in range(0,num):
        rnd = random.randint(0,9)
        res += ' ' + str(rnd+ (1 if normalb == 10 else 0))
        normala = min(normala, rnd)
    res += "]=" + str(normala * 10 + normalb)
    return res