import os
import sys
import cv2
import glob

def histogram_equalization(img):

    """
    ENTER YOUR CODE HERE
    """
    
    """
    SAMPLE SOLUTION - MAY NOT BE THE BEST SOLUTION

    img = cv2.equalizeHist(img)
    """
    
    return img


if __name__ == '__main__':

    output_dir = os.path.join(os.getcwd(), 'output', 'Question 4')
    input_dir = os.path.join(os.getcwd(), 'input', 'Question 4')

    files = glob.glob(os.path.join(input_dir, '*.png'))

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    for file in files:

        img = cv2.imread(file, 0)

        img = histogram_equalization(img)

        cv2.imwrite(os.path.join(output_dir, os.path.basename(file)), img)