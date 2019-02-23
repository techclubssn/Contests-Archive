import os
import sys
import cv2
import glob

def count_people(img):

    """
    ENTER YOUR CODE HERE
    """

    """
    SAMPLE SOLUTION - MAY NOT BE THE BEST SOLUTION

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(img, 1.3, 7)
    count = len(faces)
    """
    
    return count

if __name__ == '__main__':

    output_dir = os.path.join(os.getcwd(), 'output', 'Question 5')
    input_dir = os.path.join(os.getcwd(), 'input', 'Question 5')

    files = glob.glob(os.path.join(input_dir, '*.png'))

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    counter = []
    for file in files:

        img = cv2.imread(file, 0)

        count = count_people(img)

        counter.append(count)

    with open(os.path.join(output_dir, 'output.txt'), 'w') as file:
        file.write(str(counter))
