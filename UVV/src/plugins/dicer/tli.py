#终止节点，返回字符串
import random
from ..common.CommonFunc import *
from ..common.Message import *
from .CardManager import *

from nonebot.adapters.cqhttp import Bot, Event

ticmd = on_dicerCmd("ti", 2)
@ticmd.handle()
async def tihandle(bot: Bot, event: Event):
    await ticmd.finish(GetCardName(bot, event) + ti())


licmd = on_dicerCmd("li", 2)
@licmd.handle()
async def lihandle(bot: Bot, event: Event):
    await licmd.finish(GetCardName(bot, event) + li())



def ti():
    i = random.randint(1, 10)
    r = " 的临时疯狂判定1D10=%d\n" % i
    r += temporary_madness[i-1]
    if i == 9:
        j = random.randint(1, 100)
        r += "\n恐惧症状为：\n"
        r += phobias[j-1]
    elif i == 10:
        j = random.randint(1, 100)
        r += "\n狂躁症状为：\n"
        r += manias[j-1]
    r += "\n该症状将会持续1D10=%d" % random.randint(1, 10)
    return r


def li():
    i = random.randint(1, 10)
    r = " 的总结疯狂判定1D10=%d\n" % i
    r += madness_end[i-1]
    if i in [2, 3, 6, 9, 10]:
        r += "\n调查员将在1D10=%d小时后醒来" % random.randint(1, 10)
    if i == 9:
        j = random.randint(1, 100)
        r += "\n恐惧症状为：\n"
        r += phobias[j-1]
    elif i == 10:
        j = random.randint(1, 100)
        r += "\n狂躁症状为：\n"
        r += manias[j-1]
    return r