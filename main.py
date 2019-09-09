import sys
# -*- coding: utf-8 -*-
# __author__=StevenQi 1844697834@qq.com
sys.path.append('py_aiplat_demo\\SDK')
import apiutil
import time
import json
class mapi:
    app_key="lNQheReF4AErb5IE"
    app_id="2114340099"
    count=1
    def chatLOG(self,st):
        fp=open("chat.log","w+")
        print("\n")
        fp.write("___________________")
        fp.write(time.asctime())
        fp.write(self.app_id)
        fp.write(self.app_key)
        fp.write("___________________")
        fp.write("error:"+st.encode("utf-8"))

    def getWordTEST(self,st):
        print(time.asctime())
        print("NOW START TO TEST THE AI CHAT")
        api_obj=apiutil.AiPlat(self.app_id,self.app_key)
        type=10000
        rsp = api_obj.getNlpTextChat(type,st)
        if rsp['ret'] == 0:
            print("success")
            print(rsp['data']['answer'])
        else:
            print("failed")
            print(rsp['ret'])
            print(json.dumps(rsp, ensure_ascii=False, sort_keys=False, indent=4))
    def TransWord(self,st):
        print("翻译开始")
        api_obj=apiutil.AiPlat(self.app_id,self.app_key)
        type=0
        print("打开连接")
        rsp = api_obj.getNlpTextChat(type,st)
        if rsp['ret'] == 0:
            print("成功")
            print(json.dumps(rsp, ensure_ascii=False, sort_keys=False, indent=4))
            print(rsp['data']['answer'])
        else:
            print("失败")
            print(rsp['ret'])
            #self.chatLOG(rsp['ret'])
            print(json.dumps(rsp, ensure_ascii=False, sort_keys=False, indent=4))
            print("exit code 0")
            exit(0)
    def getWord(self,st):
        api_obj=apiutil.AiPlat(self.app_id,self.app_key)
        type=10000
        rsp = api_obj.getNlpTextChat(type,st)
        if rsp['ret'] == 0:
            print(rsp['data']['answer'])
        else:
            print("failed")
            print(rsp['ret'])
            print(json.dumps(rsp, ensure_ascii=False, sort_keys=False, indent=4))
    def changekey(self,key2):
        self.app_key=key2
    def changeID(self,ID2):
        self.app_id=ID2;

if __name__ == "__main__":
    print("this modle is used as main fucntion")
    mp1=mapi()
    mp1.getWordTEST("你好")
    a=""
    a=raw_input(">_:".encode("utf-8"));
    while(a!="exit"):
        mp1.getWord(a)
        a=raw_input(">_:".encode("utf-8"));

