#一些公用函数
from nonebot.plugin import on_startswith,on_regex
from nonebot.adapters.cqhttp import Bot, Event
from .Message import *
import re

def IsGroupMessage(bot: Bot, event: Event):
    return event.get_event_name().startswith("message.group")


def GetGroupId(bot: Bot, event: Event):
    if not IsGroupMessage(bot, event):
        return 0
    return event.group_id

def on_dicerCmd(s, p):
    '''
    用正则匹配一下开头的中文句号以及忽略大小写
    已经帮忙加了开头的点了，s直接填指令就行
    '''
    return on_regex("^(。|\.)" + s, re.I, priority=p)

def GetMessageByName(name):
	if Messages[name] != None:
		return Messages[name]
	else:
		return "Undefined Message : " + name

def FormatMessageByName(name, dict):
    if Messages[name] != None:
        try:
            return Messages[name].format(**dict)
        except Exception as e:
            return "Undefined Parameters :" + str(e)
    else:
        return "Undefined Message : " + name
