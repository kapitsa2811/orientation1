#from deskew import determine_skew
from skimage import io
from deskew.deskew import determine_skew
import os
from PIL import Image, ImageOps
import pandas as pd


actualAngle=-45

dirPath="/home/k/PycharmProjects/pythonProject/kerasOCR/masterCard/imagePreprocessing/ori/ori//"+str(actualAngle)+"//"
dirPath="/home/k/PycharmProjects/pythonProject/kerasOCR/masterCard/Alyn/deskew/tests//"+str(actualAngle)+"//"
df=pd.DataFrame(columns=["imageName","newName","actualRotationAngle","predictedRotationAngle","ascii","text"])


for indx,nm in enumerate(os.listdir(dirPath)):

        if nm.endswith(".png"):
                try:

                        print("\n\t nm:",nm,"\t indx:",indx)
                        angle=determine_skew(io.imread(dirPath+nm))

                        print("\n\t angle:",angle,"\t actual angle:",actualAngle)

                        tempDir = {"imageName": str(nm), "actualRotationAngle": str(actualAngle),
                                   "predictedRotationAngle": str(angle),
                                   "ascii":"", "newName": "", "text":""}
                        dfRow = pd.DataFrame(tempDir, index=[0])
                        df = df.append(dfRow, ignore_index=True)


                        '''
                        im1 = Image.open(dirPath+nm)
                        im2 = ImageOps.grayscale(im1)
                        im2.save(dirPath+nm)
                        '''

                except Exception as e:
                        print("\n\t e:",e)
                        pass

df.to_csv(dirPath+"//rotationReport_"+str(actualAngle)+"_.csv")