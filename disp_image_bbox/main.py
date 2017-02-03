'''
Created on Jan 6, 2017

@author: jumabek
'''
from os import listdir
from os.path import isfile, join
import argparse
import cv2
import numpy as np


def read_annotations(filename):
    f = open(filename,'r')
    num_of_lines = int(f.readline().rstrip('\n')) #actually we do not need this 
    annotations =[]
    for i in range(num_of_lines):
        annotations.append(f.readline().rstrip('\r\n'))
            
    return annotations    
    
def draw_annos(image,annos):
    for i in range(len(annos)):
        bbox_str = annos[i].split(' ')
        bbox_int = [int(v) for v in bbox_str]
        [x,y,w,h] = bbox_int    
        cv2.rectangle(image,(x,y),(w,h),(0,0,255))


parser = argparse.ArgumentParser()
parser.add_argument('-images_root', type=str,required = True, 
                    help='path to root of the images dir')
parser.add_argument('-annos_root', type=str, required = True, 
                    help='path to root of the annotations dir')

args = parser.parse_args()


print "images_root you provided {}".format(args.images_root)
print "annos_root you provided is {}".format(args.annos_root)


imagefiles = [f for f in listdir(args.images_root) if isfile(join(args.images_root, f))]

annotations = [f for f in listdir(args.annos_root) if isfile(join(args.annos_root,f))]
annotations = np.array(annotations)
annotations = np.sort(annotations)

#filtering '*.jpg' files
imagefiles = [image_file for image_file in imagefiles if image_file[image_file.rfind('.')+1:]=='JPEG']
imagefiles = np.array(imagefiles)
imagefiles = np.sort(imagefiles)


print annotations.shape
print annotations.shape

for i in range(imagefiles.shape[0]):
    im = cv2.imread(join(args.images_root,imagefiles[i]))
    annos = read_annotations(join(args.annos_root,annotations[i]))
    print annos
    
    draw_annos(im,annos)
    cv2.imshow('image',im)
    cv2.waitKey(700)
