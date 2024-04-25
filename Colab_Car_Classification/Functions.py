import os 
import re
import cv2
import csv
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def resize(raw_path=None, resize_path=None, height=128, width=128):
    file_list = os.listdir(raw_path)
    file_name = []
    for i in file_list:
        a = int(re.sub('[^0-9]', '', i))  
        file_name.append(a)

    for i, k in enumerate(file_list):
        img = cv2.imread(raw_path + '\\' + k)
        resize_img1 = cv2.resize(img, (height, width), interpolation=cv2.INTER_CUBIC)
        x = str(file_name[i])
        cv2.imwrite(resize_path + "/" + x + ".jpg", resize_img1)     

    plt.imshow(resize_img1)
    plt.show()  
    print("img shape", resize_img1.shape)  
    


def image_load(path):
    file_list = os.listdir(path)
    
    file_name = []
    for i in file_list:
        a = int(re.sub('[^0-9]', '', i)) 
        
        file_name.append(a)
    file_name.sort()  
    
    file_res = []
    for j in file_name:
        file_res.append('%s/%d.jpg' %(path,j) )
    
    image = []
    for k in file_res:
        img = cv2.imread(k)
        image.append(img)
    
    return np.array(image)


def csv_maker_84(path, k1=None, k2=None):
    file = open(path, 'w')
    
    for i in range(k1):   #k1=84
        for j in range(k2):   #k2=360
            file.write(str(i) + '\n')

    file.close

    
def csv_maker_5(path, k1=None, k2=None, k3=None, k4=None, k5=None):
    file = open(path, 'w')
    
    for i in range(k1):
        file.write(str(0) + '\n')
    for i in range(k2):
        file.write(str(1) + '\n')
    for i in range(k3):
        file.write(str(2) + '\n')
    for i in range(k4):
        file.write(str(3) + '\n')
    for i in range(k5):
        file.write(str(4) + '\n')      
     
    file.close
    
   
def label_load(path, label_cnt=None):

    file = open(path)
    labeldata = csv.reader(file)
    labellist = list(labeldata)
    label = np.array(labellist)
    label = label.astype(int)
    label = np.eye(label_cnt)[label]
    label = label.reshape(-1,label_cnt)
    return label






























