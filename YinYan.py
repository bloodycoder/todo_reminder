# -*- coding: utf-8 -*-
import random
import json
import PicardMail
def main():
    f = open("set.xml")
    text = json.load(f)
    possibleYin = text["yinPercent"]
    if(random.random()<possibleYin):
        sentArray = text["yin"]
    else:
        sentArray = text["yan"]
    textToSent = sentArray[random.randint(0,len(sentArray)-1)]
    robot = PicardMail.PicardSendMail()
    robot.Login()
    robot.SendAnEmail(email=textToSent,subject="阴阳预告",destination="510297127@qq.com")
    robot.Quit()
main()
