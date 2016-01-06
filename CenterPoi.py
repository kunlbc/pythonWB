#-------------------------------------------------------------------------------
# Name:        CenterPoi
# Purpose:     To get the point of the grid
#
# Author:      XGT
#
# Created:     06/01/2016
# Copyright:   (c) XGT 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def GenerGrid(leftBottom,topRight,column,row):
    poiList=[]
    if len(leftBottom)==2 and len(topRight)==2:
        west=leftBottom[0]
        south=leftBottom[1]
        east=topRight[0]
        north=topRight[1]
        if column!=0 and row !=0:
            columnGap=(east-west)/column
            rowGap=(north-south)/row
            #west+=columnGap/2
            #south+=rowGap/2
            #poiList.append([west,south])
            for i in range(0,row):
                #tempX=west
                #tempY=south
                for j in range(0,column):
                    tempX=west+columnGap/2+columnGap*j
                    tempY=south+rowGap/2+rowGap*i
                    #tempX=west+columnGap*j
                    poiList.append([tempX,tempY])
                #tempY=south+rowGap*i
                #poiList.append([tempX,tempY])
    return poiList

def main():
    leftBottom=[116.270,39.830]
    topRight=[116.498,39.993]
    column=7
    row=7
    poiList=GenerGrid(leftBottom,topRight,column,row)
    text=""
    if len(poiList)!=0:
        for item in poiList:
            text+=str(item[0])+","+str(item[1])+"\n"
        open('centerPoi.txt','a').write(text)

if __name__ == '__main__':
    main()
    print 'done'
