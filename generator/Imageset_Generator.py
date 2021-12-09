import os
import random
# Import lib of DOM to resolve XML files
from xml.dom.minidom import parse

# User Inputs
trainval_percent = 0.9
train_percent = 0.8

jpgfilepath = '../dataset/VOCdevkit/VOC2012/JPEGImages'
txtsavepath = '../dataset/VOCdevkit/VOC2012/ImageSets/Main'
ftest_path = '/home/sfmt/DuDu_Bench/10_Project/Experiment-211006_Philips_Bottle_Labelling/Dataset/VOC2007/ImageSets/Main/test.txt'
ftrain_path ='/home/sfmt/DuDu_Bench/10_Project/Experiment-211006_Philips_Bottle_Labelling/Dataset//VOC2007/ImageSets/Main/train.txt'
fval_path = '/home/sfmt/DuDu_Bench/10_Project/Experiment-211006_Philips_Bottle_Labelling/Dataset/VOC2007/ImageSets/Main/val.txt'
ftrainval_path = '/home/sfmt/DuDu_Bench/10_Project/Experiment-211006_Philips_Bottle_Labelling/Dataset/VOC2007/ImageSets/Main/trainval.txt'


# dom = parse(xmlfilepath)
# data = dom.documentElement
# images = data.getElementsByTagName('image')
# num = len(images)
# print("Total image number:", num)

target_jpgs = os.listdir(jpgfilepath)
num = len(target_jpgs)
list = range(num)
tv = int(num*trainval_percent)
tr = int(tv*train_percent)
trainval = random.sample(list,tv)
train = random.sample(trainval,tr)

ftrainval = open(ftrainval_path, 'w')
ftest = open(ftest_path, 'w')
ftrain = open(ftrain_path, 'w')
fval = open(fval_path, 'w')

for i in list:
	name = target_jpgs[i]+'\n'
	if i in trainval:
		ftrainval.write(name)
		if i in train:
			ftrain.write(name)
		else:
			fval.write(name)
	else:
		ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
