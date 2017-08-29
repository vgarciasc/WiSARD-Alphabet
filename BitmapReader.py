from PIL import Image
import numpy as np

def getImageAsPixels(filename):
    try:
        im = Image.open(filename)
    except FileNotFoundError as e:
        print(e)
        exit()
    
    matrix = np.asarray(im)
    linearArray = []

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            pixel = matrix[i][j][0]
            if pixel == 255:
                pixel = 1
            else:
                pixel = 0
            linearArray.append(pixel)

    return linearArray