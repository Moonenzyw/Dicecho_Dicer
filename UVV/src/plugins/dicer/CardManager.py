from nonebot.adapters.cqhttp import Bot, Event
from ..common.CommonFunc import *

card = {}
def GetCardName(bot: Bot, event: Event):
    '''
    获取当前QQ的人物卡名。
    如果没有对应的人物卡，则返回群名片。
    如果没有群名片，则返回昵称。
    '''
    qqid = int(event.sender.user_id)
    if qqid in card:
        return card[qqid]["name"]
    if IsGroupMessage(bot, event):
        return event.sender.card
    return event.sender.nickname

def GetCardAttribute(bot: Bot, event: Event, att : str):
    '''
    获取key为att的属性，返回值应该为int
    如果当前没有人物卡或者人物卡没有对应的属性， 返回-1
    '''
    qqid = int(event.sender.user_id)
    if qqid in card:
        return card[qqid][att]
    return -1
