"""
Character Detection
(Due date: March 8th, 11: 59 P.M.)

The goal of this task is to experiment with template matching techniques. Specifically, the task is to find ALL of
the coordinates where a specific character appears using template matching.

There are 3 sub tasks:
1. Detect character 'a'.
2. Detect character 'b'.
3. Detect character 'c'.

You need to customize your own templates. The templates containing character 'a', 'b' and 'c' should be named as
'a.jpg', 'b.jpg', 'c.jpg' and stored in './data/' folder.

Please complete all the functions that are labelled with '# TODO'. Whem implementing the functions,
comment the lines 'raise NotImplementedError' instead of deleting them. The functions defined in utils.py
and the functions you implement in task1.py are of great help.

Hints: You might want to try using the edge detectors to detect edges in both the image and the template image,
and perform template matching using the outputs of edge detectors. Edges preserve shapes and sizes of characters,
which are important for template matching. Edges also eliminate the influence of colors and noises.

Do NOT modify the code provided.
Do NOT use any API provided by opencv (cv2) and numpy (np) in your code.
Do NOT import any library (function, module, etc.).
"""


import argparse
import json
import os

import numpy as np
import cv2

import utils
from task1 import *   # you could modify this line


def parse_args():
    parser = argparse.ArgumentParser(description="cse 473/573 project 1.")
    parser.add_argument(
        "--img_path", type=str, default="./data/characters.jpg",
        help="path to the image used for character detection (do not change this arg)")
    parser.add_argument(
        "--template_path", type=str, default="",
        choices=["./data/a.jpg", "./data/b.jpg", "./data/c.jpg"],
        help="path to the template image")
    parser.add_argument(
        "--result_saving_directory", dest="rs_directory", type=str, default="./results/",
        help="directory to which results are saved (do not change this arg)")
    args = parser.parse_args()
    return args


def detect(img, template):
    """Detect a given character, i.e., the character in the template image.

    Args:
        img: nested list (int), image that contains character to be detected.
        template: nested list (int), template image.

    Returns:
        coordinates: list (tuple), a list whose elements are coordinates where the character appears.
            format of the tuple: (x (int), y (int)), x and y are integers.
            x: row that the character appears (starts from 0).
            y: column that the character appears (starts from 0).
    """
    # TODO: implement this function.
    print(np.shape(img))
    print(np.shape(template))
    img_r = len(img)
    img_c = len(img[0])
    print(img_r,img_c)
    temp_r = len(template)
    temp_c = len(template[0])
    print(temp_r,temp_c)
    diff = []
    diff_elem = []
    sum = 0
    #img = np.int64(img)
    m=0
    n=0
    min =5
    max =0
    #print(template)
    #print(img)
    #cv2.imshow('image',np.array(img))
    #cv2.waitKey(0)
    for i in range(0,img_r - (temp_r)):
        for j in range(0, img_c - (temp_c)):
            m = 0
            #print("i value" + str(i), "j value"+str(j))
            
            for k in range(i, i+temp_r):
                for l in range(j, j+temp_c):
                    #print("k value" + str(k),"l value"+str(l) )
                    #print(abs(template[m][n] - img[k][l]))
                    #sum  = sum + (template[m][n] - img[k][l])**2
                    #print(sum)
                    #if(sum < min):
                    #    print("k value" + str(k),"l value"+str(l),"sum "+str(sum) )

                    n = n+1
                n=0
                m = m+1
            diff_elem.append(sum)
            sum = 0
        diff.append(diff_elem)
        diff_elem=[]
    #print(diff[307][478])
    #raise NotImplementedError
    #print(diff)
    print("In detect")
    print(np.shape(diff))
    x = len(diff)
    y = len(diff[0])
    print(x,y)
    l_x = 0
    l_y = 0
    '''
    img2 = img
    for i in range(0,x):
        for j in range(0,y):
            if(diff[i][j]<min):
                min = diff[i][j]
                l_x,l_y = i,j
                #print(min,l_x,l_y)
                #cv2.rectangle(np.array(img2),(l_x,l_y),(l_x+temp_r-1,l_y+temp_c-1),(255,255,255),10)
    print(min)
    '''
    #cv2.imshow('image',np.array(img2))
    #cv2.waitKey(0)

    raise NotImplementedError
    return coordinates

def Ncc()


def save_results(coordinates, template, template_name, rs_directory):
    results = {}
    results["coordinates"] = sorted(coordinates, key=lambda x: x[0])
    results["templat_size"] = (len(template), len(template[0]))
    with open(os.path.join(rs_directory, template_name), "w") as file:
        json.dump(results, file)


def main():
    args = parse_args()

    img = read_image(args.img_path)
    template = read_image(args.template_path)

    coordinates = detect(img, template)

    template_name = "{}.json".format(os.path.splitext(os.path.split(args.template_path)[1])[0])
    save_results(coordinates, template, template_name, args.rs_directory)


if __name__ == "__main__":
    main()
