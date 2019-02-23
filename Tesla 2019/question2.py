import os
import sys
import cv2
import glob

def remove_noise(img):

    """
    ENTER YOUR CODE HERE
    """

    """
    SAMPLE SOLUTION - MAY NOT BE THE BEST SOLUTION

    img = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
    """
    
    return img

if __name__ == '__main__':

    output_dir = os.path.join(os.getcwd(), 'output', 'Question 2')
    input_dir = os.path.join(os.getcwd(), 'input', 'Question 2')

    files = glob.glob(os.path.join(input_dir, '*.png'))

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    for file in files:

        img = cv2.imread(file, 1)

        img = remove_noise(img)

        cv2.imwrite(os.path.join(output_dir, os.path.basename(file)), img)