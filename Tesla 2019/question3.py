import os
import sys
import cv2
import glob

def threshold_red(img):

    """
    ENTER YOUR CODE HERE
    """

    """
    SAMPLE SOLUTION - MAY NOT BE THE BEST SOLUTION

    img = img[:, :, 2]
    """

    return img


if __name__ == '__main__':

    output_dir = os.path.join(os.getcwd(), 'output', 'Question 3')
    input_dir = os.path.join(os.getcwd(), 'input', 'Question 3')

    files = glob.glob(os.path.join(input_dir, '*.png'))

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    for file in files:

        img = cv2.imread(file, 1)

        mask = threshold_red(img)

        cv2.imwrite(os.path.join(output_dir, os.path.basename(file)), mask)
