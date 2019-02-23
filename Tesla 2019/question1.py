import os
import sys
import cv2
import glob

def remove_salt_and_pepper(img):

    """
    ENTER YOUR CODE HERE
    """

    """
    SAMPLE SOLUTION - MAY NOT BE THE BEST SOLUTION

    img = cv2.medianBlur(img, 7)
    """
    
    return img


if __name__ == '__main__':

    output_dir = os.path.join(os.getcwd(), 'output', 'Question 1')
    input_dir = os.path.join(os.getcwd(), 'input', 'Question 1')

    files = glob.glob(os.path.join(input_dir, '*.png'))

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    for file in files:

        img = cv2.imread(file, 1)

        img = remove_salt_and_pepper(img)

        cv2.imwrite(os.path.join(output_dir, os.path.basename(file)), img)