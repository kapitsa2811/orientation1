import pandas as pd

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2
import re
import os
from copy import deepcopy

imageName="90degrees-1.png"

'''
    this finds angle
'''

def  orientationCalculation(img,path=None):

    if img:
        img=cv2.imread(path)
    #print("\n\t img :",img.shape)
    try:
        osd = pytesseract.image_to_osd(img)
        angle = re.search('(?<=Rotate: )\d+', osd).group(0)
        #script = re.search('(?<=Script: )\d+', osd).group(0)
        #print("angle: ", angle)
        #print("script: ", script)
    except Exception as e:
        return None
    return angle

'''
    this rotates image and save
'''
def rotateImage(img,angle):
    temp=img.rotate(angle)
    temp.save(savePath+imName+str(angle)+".png")
    return temp

cwd=os.getcwd()
dataPath=cwd+"//ori//data//"
savePath=cwd+"//ori//ori//"

allImages=os.listdir(dataPath)
print("\n\t allImages=",allImages)

'''
    rotate and save
'''
count5,count355,count45,count90,count135,count180=0,0,0,0,0,0


def ocrImage(temp):
    return pytesseract.image_to_string(temp)


def is_ascii(s):

    ascii_string = set("""!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~""")

    total_count = len(s)
    non_ascii_count = sum(c not in ascii_string for c in s)

    #print("\n\t s:",s)
    #return all(ord(c[0][0]) < 128 for c in s.split(" "))

    return non_ascii_count/total_count

rotateAngles=[5,10,15,30,45,90,180,345,350,355]
rotateAngles=[270]

df=pd.DataFrame(columns=["imageName","newName","actualRotationAngle","predictedRotationAngle","ascii","text"])

for indx, imName in enumerate(allImages):

    print("\n\t indx:",indx,"\t imName:",imName)
    img= Image.open(dataPath+imName)  #cv2.imread(dataPath+imName)

    temp=deepcopy(img)

    for tempAngle in rotateAngles:
        temp=rotateImage(img,tempAngle)

        '''
        txt=""
        actual1=tempAngle
        angle1=orientationCalculation(temp,savePath+imName+str(tempAngle)+".png")

        #print("\n\t indx:",indx,"\t imName:",imName)
        print("\n\t predicted angles:",angle1)
        print("\n\t Actual    angles:",tempAngle,"\t predicted:",angle1)

        if 1:#angle1==None:
            txt=ocrImage(temp)
            #print("\n\t txt:",txt)
            #print("\n\t ocr image")
            #input("check!!")
        tempDir = {"imageName": str(imName),"actualRotationAngle":str(tempAngle),"predictedRotationAngle":str(angle1),"ascii":is_ascii(txt),"newName":"","text":str(txt)}

        dfRow=pd.DataFrame(tempDir, index=[0])

        df=df.append(dfRow,ignore_index = True)
        df.to_csv(".//rotationReport.csv")
        '''

print("\n\t df:\n",df.head())

df.to_csv(".//rotationReport.csv")

#     try:
#         if int(angle1)==int(actual1):
#             count45+=1
#     except Exception as e:
#         pass
#
#     try:
#         if int(angle2)==int(actual2):
#             count90+=1
#     except Exception as e:
#         pass
#
#     try:
#         if int(angle3)==int(actual3):
#             count135+=1
#
#     except Exception as e:
#         pass
#
#     try:
#         if int(angle4)==int(actual4):
#             count180+=1
#     except Exception as e:
#         pass
#
#     print("\n\t count45:", count45, "\t count90:", count90, "\t count135:", count135, "\t count180:", count180,"\t total:",indx)
#     #print("\n\t total:", indx)
#
# print("\n\t count45:",count45,"\t count90:",count90,"\t count135:",count135,"\t count180:",count180)
# print("\n\t total:",indx)indx