#-------------------------------------------------------------------------------
# Name:        GraspData
# Purpose:     主要用来抓取全市的主要签到数据
#
# Author:      XGT
#
# Created:     06/01/2016
# Copyright:   (c) XGT 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import weibo
import webbrowser

APP_KEY='2218208544'
APP_SECRET='956ae245a2f62a11a9eca1d91fbda092'
CALLBACK_URL='http://cdgir.cumt.edu.cn/ShowCode.aspx'
Cache=[] #全局poiid

def getClient():
    client=weibo.APIClient(APP_KEY,APP_SECRET,CALLBACK_URL)
    url=client.get_authorize_url()
    webbrowser.open(url)
    code=raw_input("input the code:").strip()
    r=client.request_access_token(code);
    client.set_access_token(r.access_token,r.expires_in)
    return client

def getPointS():
    #client=getClient()
    lat_long_file=open("centerPoi.txt","r")
    for lines in lat_long_file:
        try:
            lat_long=lines.strip("\n").split(",")
            print ' '.join(lat_long)


def main():
    print "hello"

if __name__ == '__main__':
    main()
