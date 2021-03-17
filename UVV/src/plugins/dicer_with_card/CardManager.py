from nonebot.plugin import export
export = export()

card = {}
def GetCardName(bot: Bot, event: Event):
    '''
    获取当前QQ的人物卡名。
    如果没有对应的人物卡，则返回群名片。
    如果没有群名片，则返回昵称。
    '''
    qqid = event.sender.user_id
    if card[qqid]:
        return card[qqid]["name"]
    if IsGroupMessage(bot, event):
        return event.sender.card
    return event.sender.nickname

def GetCardAttribute(bot: Bot, event: Event, att : str):
    '''
    获取key为att的属性，返回值应该为int
    如果当前没有人物卡或者人物卡没有对应的属性， 返回-1
    '''
    qqid = event.sender.user_id
    if card[qqid]:
        return card[qqid][att]
    return -1

    
export.GetCardName = GetCardName