from alyn.deskew import *
from alyn.skew_detect import *
from alyn.skew_detect import  SkewDetect
#from alyn.skew_detect import importSkewDetect
#from alyn import SkewDetect

path="/home/k/PycharmProjects/pythonProject/kerasOCR/masterCard/Alyn/examples//images//"
imgName="CV_(2).jpg90.png"

dirPath="/home/k/PycharmProjects/pythonProject/kerasOCR/masterCard/Alyn/alyn/examples/images/"
imgPath="/home/k/PycharmProjects/pythonProject/kerasOCR/masterCard/Alyn/alyn/examples/images/CV_(2).jpg90.png"

for indx,nm in enumerate(os.listdir(dirPath)):
	print("\n\t indx:",indx,"\t image name:",nm)
	sd = SkewDetect(
		input_file=dirPath+nm,#path+imgName,
		batch_path='optional_batch_processing_path',
		output_file=path+"out//1.txt",
		display_output='Yes/No')
	sd.run()

	import numpy as np
	from skimage import io
	from skimage.color import rgb2gray
	from skimage.transform import rotate

	from alyn.deskew import deskew

	image = io.imread('input.png')
	grayscale = rgb2gray(image)
	angle = determine_skew(grayscale)
	rotated = rotate(image, angle, resize=True) * 255
	io.imsave('output.png', rotated.astype(np.uint8))


'''
from alyn import Deskew
d = Deskew(
	input_file=path+imgName,
	display_image='preview the image on screen',
	output_file=path+"out//",
	r_angle='offest_angle_in_degrees_to_control_orientation')
d.run()
'''
