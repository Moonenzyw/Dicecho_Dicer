import re
import random
from ..common.CommonFunc import *
from ..common.Message import *
from .CardManager import *

from nonebot.adapters.cqhttp import Bot, Event

#r，顺序在rh，ra和rd之后，优先级往后排
rcmd = on_dicerCmd("r", 3)
@rcmd.handle()
async def rhandle(bot: Bot, event: Event):
    args = str(event.get_message())[2:].strip()
    pa = {}
    pa["name"] = GetCardName(bot,event)
    pa["content"] = r(args)[0]
    await rcmd.finish(FormatMessageByName("Normal_Roll", pa))

#处理rXdY表达式
def r(args):
    try:
        if args[0] != 'd' and (args[0] < '0' or args[0] > '9'):
            return r_help_message

        #匹配所有 XdY 以及之后可能会有的+和-，包括常数
        res = re.finditer("((\\+|-)?)[0-9]*d?[0-9]+", args, re.I)
        cals = [i.group() for i in res]
        if len(cals) > 10:
            return "表达式过长。"
        fullstr = ""
        for cal in cals:
            fullstr += cal
        if not args.startswith(fullstr):
            return r_help_message


        resnum = 0
        resbegin = ""
        resend = ""
        for cal in cals:
            resbegin += cal.upper()

            sign = -1 if cal.startswith("-") else 1
            if cal[0] in ['+', '-']:
                resend += cal[0]
            cal = cal.replace("+", "").replace("-", "")

            sp = cal.split("d")
            if len(sp) == 1: #不带d是常数
                resnum += sign * int(cal)
                resend += cal.upper()
                continue

            x,y = 1,1
            if sp[0] != "":
                x = int(sp[0])
            y = int(sp[1])
            if x >= 10:
                return "同一表达式内骰点次数过多。（.rXdY的X应小于10）"
            
            xdy = 0
            resend += "(" if x > 1 else ""
            for i in range(0,x-1):
                rnd = random.randint(1,y)
                xdy += rnd
                resend += str(rnd) + "+"
            rrnd = random.randint(1,y)
            xdy += rrnd
            resend += str(rrnd) + (")" if x > 1 else "")
            resnum += xdy * sign
        
        args = args.replace(fullstr,"")
        return [args + " : " + resbegin + " = " + resend + ((" = " + str(resnum)) if len(cals) > 1 else ""), resnum]

    except:
        return r_help_message

if __name__ == "__main__":
    print(r("3"))