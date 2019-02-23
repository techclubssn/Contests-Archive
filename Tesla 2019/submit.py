import os
import cv2
import sys
import glob
import json
import numpy as np

from question1 import remove_salt_and_pepper
from question2 import remove_noise
from question3 import threshold_red
from question4 import histogram_equalization
from question5 import count_people

import firebase_admin
from firebase_admin import credentials, firestore
 
def load_dirs(question):

    input_dir = os.path.join(os.getcwd(), 'input', 'Question ' + str(question))
    answers_dir = os.path.join(os.getcwd(), 'answers', 'Question ' + str(question))

    answers = sorted(glob.glob(os.path.join(answers_dir, '*.png')))
    inputs = sorted(glob.glob(os.path.join(input_dir, '*.png')))

    return answers, inputs


def evaluate_mse(img, GT):

    max_mse_value = 255 * 255
    mse = np.square(img - GT).mean()
    score = (max_mse_value - mse) / max_mse_value

    return score

def evaluate_mask(mask, GT):

    intersection = np.count_nonzero((mask + GT) == 2)
    union = np.count_nonzero((mask + GT) >= 1)
    score = intersection / union
    
    return score

def evaluate_histogram(output, GT):

    new = np.histogram(output.ravel())[0]
    sum_ = sum(new.ravel())
    disparity = new.max() - new.min()

    score = (sum_ - disparity) / sum_

    return score

def evaluate_count(count, GT):

    score = 1 - (abs(count - GT) / (GT + 10e-12))

    return score


if __name__ == '__main__':

    ascii_art = \
    """
$$$$$$$$\ $$$$$$$$\  $$$$$$\  $$\        $$$$$$\  
\__$$  __|$$  _____|$$  __$$\ $$ |      $$  __$$\ 
   $$ |   $$ |      $$ /  \__|$$ |      $$ /  $$ |
   $$ |   $$$$$\    \$$$$$$\  $$ |      $$$$$$$$ |
   $$ |   $$  __|    \____$$\ $$ |      $$  __$$ |
   $$ |   $$ |      $$\   $$ |$$ |      $$ |  $$ |
   $$ |   $$$$$$$$\ \$$$$$$  |$$$$$$$$\ $$ |  $$ |
   \__|   \________| \______/ \________|\__|  \__|
                                                                                                    
    """

    print(ascii_art)
    print('Welcome to the Tesla Image Processing and Computer Vision contest!')

    if not os.path.exists(os.path.join(os.getcwd(), 'metadata.json')):
        print('-----------------------------------------------')
        print('Please register before submitting your results.')
        print('You can register by running: python register.py')
        print('-----------------------------------------------')
        sys.exit(0)

    with open('metadata.json', 'r') as file:
        metadata = json.load(file)


    print('---------------------------')
    print('Evaluating you submissions:')
    print('---------------------------')

    offset_1 = 33

    all_scores = []
    answers, inputs = load_dirs(1)
    total_score = 0

    for i, (img_file, answer) in enumerate(zip(inputs, answers), 1):

        GT = cv2.imread(answer, 1)
        img = cv2.imread(img_file, 1)

        try:
            img  = remove_salt_and_pepper(img)
            score = evaluate_mse(img, GT)
        except:
            print('Looks like something is wrong with Question 1 submission -- Score of 0 is provided for test case '+str(i))
            score = 0

        ## More weightage for test cases
        total_score += score * (1 + (i > 3))

    ## Converting to 30 marks
    total_score = (total_score / 9) * 30
    all_scores.append(total_score)
    print('Question 1:', total_score)

    answers, inputs = load_dirs(2)
    total_score = 0

    for i, (img_file, answer) in enumerate(zip(inputs, answers), 1):

        GT = cv2.imread(answer, 1)
        img = cv2.imread(img_file, 1)

        try:
            img  = remove_noise(img)
            score = evaluate_mse(img, GT)
        except:
            print('Looks like something is wrong with Question 2 submission -- Score of 0 is provided for test case '+str(i))
            score = 0

        ## More weightage for test cases
        total_score += score * (1 + (i > 3))

    ## Converting to 30 marks
    total_score = (total_score / 9) * 30
    all_scores.append(total_score)
    print('Question 2:', total_score)

    offset_2 = 127

    answers, inputs = load_dirs(3)
    total_score = 0

    for i, (img_file, answer) in enumerate(zip(inputs, answers), 1):

        GT = cv2.imread(answer, 0) / 255
        img = cv2.imread(img_file, 1)

        try:
            mask = threshold_red(img) / 255
            score = evaluate_mask(mask, GT)
        except:
            print('Looks like something is wrong with Question 3 submission -- Score of 0 is provided for test case '+str(i))
            score = 0

        ## More weightage for test cases
        total_score += score * (1 + (i > 3))

    ## Converting to 30 marks
    total_score = (total_score / 9) * 30
    all_scores.append(total_score)
    print('Question 3:', total_score)

    answers, inputs = load_dirs(4)
    total_score = 0

    for i, (img_file, answer) in enumerate(zip(inputs, answers), 1):

        GT = cv2.imread(answer, 0)
        img = cv2.imread(img_file, 0)

        try:
            img = histogram_equalization(img)
            score = evaluate_histogram(img, GT)
        except:
            print('Looks like something is wrong with Question 4 submission -- Score of 0 is provided for test case '+str(i))
            score = 0

        ## More weightage for test cases
        total_score += score * (1 + (i > 3))

    ## Converting to 30 marks
    total_score = (total_score / 9) * 30
    all_scores.append(total_score)
    print('Question 4:', total_score)

    _, inputs = load_dirs(5)

    offset = offset_1 + offset_2 + 73

    with open(os.path.join(os.getcwd(), 'answers', 'Question 5', 'count.txt'), 'r') as file:
        values = file.read().strip().split('/')

    decode = lambda x: int(x, 16) - offset
    values = list(map(decode, values))
    total_score = 0

    for i, (img_file, answer) in enumerate(zip(inputs, answers), 1):

        GT = values[i-1]
        img = cv2.imread(img_file, 0)

        try:
            count = count_people(img)
            score = evaluate_count(count, GT)
        except:
            print('Looks like something is wrong with Question 5 submission -- Score of 0 is provided for test case '+str(i))
            score = 0

        ## More weightage for test cases
        total_score += score * (1 + (i > 3))

    ## Converting to 30 marks
    total_score = (total_score / 9) * 30
    all_scores.append(total_score)
    print('Question 5:', total_score)

    print('-------------------')
    print('Submitting Results:')
    print('-------------------')
    print('You can submit results any number of times you want to. ')
    print('We will only consider the final submission regardless of its score.')
    choice = input('Would you like to submit your scores? (Y/N) ')
    print('--------------------------------------------')

    if choice == 'y' or choice == 'Y':

        print('Submitting...')
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ENTER YOUR GOOGLE CREDS HERE'
        cred = credentials.ApplicationDefault()
        firebase_admin.initialize_app(cred, {
          'projectId': 'ENTER YOUR FIREBASE PROJECT ID HERE',
        })

        db = firestore.client()

        doc_ref = db.collection('submissions').document(metadata['reg_num'])
        doc_ref.set({
            'question1': all_scores[0],
            'question2': all_scores[1],
            'question3': all_scores[2],
            'question4': all_scores[3],
            'question5': all_scores[4],
            'name': metadata['name'],
            'id': metadata['id'],
            'dept': metadata['dept'],
            'year': metadata['year']
        })
        print('Done!')

    else:

        print('Not Submitted.')
