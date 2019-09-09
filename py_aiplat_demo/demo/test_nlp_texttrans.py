#-*- coding: UTF-8 -*-
import sys
sys.path.append('../SDK')  
import optparse
import time
import apiutil
import json

app_key = 'xxx'
app_id = 'xxx'

if __name__ == '__main__':
    str_text = '今天天气怎么样'
    type = 0
    ai_obj = apiutil.AiPlat(app_id, app_key)

    print '----------------------SEND REQ----------------------'
    rsp = ai_obj.getNlpTextTrans(str_text, type)
    if rsp['ret'] == 0:
        print json.dumps(rsp, encoding="UTF-8", ensure_ascii=False, sort_keys=False, indent=4)
        print '----------------------API SUCC----------------------'
    else:
        print json.dumps(rsp, encoding="UTF-8", ensure_ascii=False, sort_keys=False, indent=4)
        # print rsp
        print '----------------------API FAIL----------------------'

