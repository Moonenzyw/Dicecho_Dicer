import random
import re
from ..common.CommonFunc import *
from ..common.Message import *
from .CardManager import *
from .rXdY import *

sccmd = on_dicerCmd("sc", 2)
@sccmd.handle()
async def schandle(bot: Bot, event: Event):
    args = str(event.get_message())[3:].strip()

    #分离sc参数
    sp = args.split(' ')
    print(sp)
    sannum = 0
    if len(sp) == 1:
        sannum = GetCardAttribute(bot,event, "san")
    elif len(sp) == 2:
        sannum = int(sp[1])
        
    pa = {}
    pa["name"] = GetCardName(bot,event)
    pa["content"] = sancheck(sannum, sp[0])
    await sccmd.finish(FormatMessageByName("SanCheck", pa))

def sancheck(sannum : int, args : str):
    try:
        if sannum <= 0:
            return "人物卡未设置且未给定检定san值。"
        
        rnd = random.randint(1,100)
        res = "\nD100=" + str(rnd)
        ssp = args.split("/")
        if len(ssp) != 2:
            return sc_help_message
        
        rres = []
        if rnd <= sannum:
            res += " 成功\n"
            rres = r(ssp[0])
        else:
            res += " 失败\n"
            rres = r(ssp[1])
        
        res += "理智减少" + rres[0] + "点，目前剩余" + str(sannum - rres[1]) + "点。"
        return res
    except:
        return sc_help_message