'''
Created on Jan 18, 2017

@author: jumabek
'''

if __name__ == '__main__':
    pass

import argparse

import cv2

parser = argparse.ArgumentParser()
parser.add_argument('-image_file', type=str,required = True, 
                    help='path to image file name')
parser.add_argument('-annotation_file', type=str, required = True, 
                    help='path to annotation file name for that image')

args = parser.parse_args()


im = cv2.imread(args.image_file)
annotation_stream = open(args.annotation_file,'r')

bboxes = [annotation.rstrip("\n\r")[1:-1] for annotation in annotation_stream.readlines()]

for bbox in bboxes:
    print bbox
    pos = [int(float(coord)) for coord in bbox.split(',')] 
    cv2.rectangle(im,(pos[0],pos[1]),(pos[0]+pos[2],pos[1]+pos[3]),(0,0,255),3);
cv2.imshow('annoation',im);

cv2.waitKey(10000);
cv2.imwrite("annotation.jpg",im);





