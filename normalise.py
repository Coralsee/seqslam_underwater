import time
import os
import shutil
from seqslam import *
from PIL import Image

def normalise():

    path = os.environ['DATASET_1_PATH']
 
    for count, filename in enumerate(sorted(os.listdir(path  + ".raw/")), start=1):
        dst ="images-%05d.png" % (count,)
        src = filename
        shutil.copy2(path + ".raw/" + src, path + "/" + dst) 

        '''basewidth = 64
        img = Image.open(path + "/" + dst)
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), Image.ANTIALIAS)
        img.save(path + "/" + dst) '''


    path = os.environ['DATASET_2_PATH']
      
    for count, filename in enumerate(sorted(os.listdir(path  + ".raw/")), start=1):
        dst ="images-%05d.png" % (count,)
        src = filename
        shutil.copy2(path + ".raw/" + src, path + "/" + dst) 
        '''basewidth = 64
        img = Image.open(path + "/" + dst)
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), Image.ANTIALIAS)
        img.save(path + "/" + dst) '''

if __name__ == "__main__":
    normalise()
