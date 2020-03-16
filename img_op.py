# extract and plot each detected face in a photograph
from matplotlib import pyplot
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle
from mtcnn.mtcnn import MTCNN
import cv2
import fnmatch
import os
detector = MTCNN()

def draw_faces(filename, result_list):
    # load the image
    data = pyplot.imread(filename)
    # plot each face as a subplot
    for i in range(len(result_list)):
        # get coordinates
        x1, y1, width, height = result_list[i]['box']
        x2, y2 = x1 + width, y1 + height
        string = "X"+str(i)+filename

        crop_img = data[y1:y1+height, x1:x1+width]
        image_to_write = cv2.cvtColor(crop_img, cv2.COLOR_RGB2BGR)
        cv2.imwrite(string,image_to_write)

import fnmatch
import os
for i in range(500):
    filename = "sahrukh_"+str(i+1)+".jpg"
    print(filename)
    try:
        pixels = cv2.imread(filename)
        detector = MTCNN()
        faces = detector.detect_faces(pixels)
        draw_faces(filename, faces)
    except:
        print("pay nai")
