import os
import sys

path = os.getcwd()+"/dont_remove/"


primaryContents = os.listdir(path)

for i in primaryContents:
    if(os.path.isdir(path+i)):
        imageList = os.listdir(path+i+"/.image/")
        for image in imageList:
            os.popen('cp ' + path+i+"/.image/"+image+" " +
                     os.getcwd()+"/images/"+image+".png")
for i in primaryContents:
    if(os.path.isdir(path+i)):
        imageList = os.listdir(path+i+"/.video/")
        for image in imageList:
            os.popen('cp ' + path+i+"/.video/"+image+" " +
                     os.getcwd()+"/videos/"+image+".mp4")
