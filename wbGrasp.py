﻿#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      XGT
#
# Created:     06/01/2016
# Copyright:   (c) XGT 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import weibo
import webbrowser
import json
import time

APP_KEY='2218208544'
APP_SECRET='956ae245a2f62a11a9eca1d91fbda092'
CALLBACK_URL='http://cdgir.cumt.edu.cn/ShowCode.aspx'
Cache=[] #全局poiid
totalPoints=0

def getClient():
    client=weibo.APIClient(APP_KEY,APP_SECRET,CALLBACK_URL)
    url=client.get_authorize_url()
    webbrowser.open(url)
    code=raw_input("input the code:").strip()
    r=client.request_access_token(code);
    client.set_access_token(r.access_token,r.expires_in)
    return client



def getPoints():
    lat_long_file=open("centerPoi.txt","r")
    pointList=[]
    for lines in lat_long_file:
        lat_long=lines.strip("\n").split(",")
        #print ','.join(lat_long)+"\n"
        pointList.append(lat_long)
    return pointList

def getPointID():
    pid_file=open("pointIDs.txt",'r')
    cache=[]
    for lines in pid_file:
        cache.append(lines.strip("\n"))
    return cache

def run(index):
    client=getClient()
    pointList=getPoints()
    text=""
    timeCount=0
    for item in pointList:
        lon=item[0]
        lat=item[1]
        page=1
        count=50
        poi_result=client.place.nearby.pois.get(lat=lat,long=lon,count=count,page=page)
        requestNum=1
        total_number=poi_result.total_number
        #print total_number
        #tmpCache=getPointID()
        #tmp=[]
        if (total_number>0) and (int(total_number)%count!=0):
            page=int(total_number)/count+1
        else:
            page=int(total_number)/count

        if poi_result.has_key('pois'):
            for val in poi_result.pois:
                if val.poiid in Cache:
                    pass
                else:
                    Cache.append(val.poiid)
                    text+="%s, %s, %s %s, %s, %s, %s, %s\n" % (val.poiid,val.checkin_num,val.title,val.lon,val.lat,val.categorys,val.category_name,val.address)
            if page==1:
                return
            else:
                for pn in range(2,page+1):
                    poi_result=client.place.nearby.pois.get(lat=lat,long=lon,count=count,page=pn)
                    if poi_result.has_key('pois'):
                        for val in poi_result.pois:
                            if val.poiid in Cache:
                                pass
                            else:
                                Cache.append(val.poiid)
                                text+="%s, %s, %s %s, %s, %s, %s, %s\n" % (val.poiid,val.checkin_num,val.title,val.lon,val.lat,val.categorys,val.category_name,val.address)
        fileName="poi"+index+".txt"
        open(fileName,'a').write(text.encode('utf-8'))
        text=""
        #pointIDs='\n'.join(tmp)+"\n"
        #open("pointIDs.txt",'a').write(pointIDs)
        print "done Well!"
        timeCount+=1
        if timeCount%10==0:
            time.sleep(1200)#这个半个小时的设置还没有进行验证 后面可进行修改
        else:
            time.sleep(20)
        #time.sleep(20)
    open("pointIDs.txt",'a').write('\n'.join(Cache))
    print "done the whole work!"



def main():
    for i in range(10):
        run(str(i))
        time.sleep(1800)

if __name__ == '__main__':
    main()
