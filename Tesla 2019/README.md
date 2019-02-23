# Image Processing and Computer Vision Contest - Tesla 2019

```
$$$$$$$$\ $$$$$$$$\  $$$$$$\  $$\        $$$$$$\  
\__$$  __|$$  _____|$$  __$$\ $$ |      $$  __$$\ 
   $$ |   $$ |      $$ /  \__|$$ |      $$ /  $$ |
   $$ |   $$$$$\    \$$$$$$\  $$ |      $$$$$$$$ |
   $$ |   $$  __|    \____$$\ $$ |      $$  __$$ |
   $$ |   $$ |      $$\   $$ |$$ |      $$ |  $$ |
   $$ |   $$$$$$$$\ \$$$$$$  |$$$$$$$$\ $$ |  $$ |
   \__|   \________| \______/ \________|\__|  \__|
```

## Description

- This repository contains code that sets up a contest based on Image Processing and Computer Vision for students.
- Students are presented with five questions where they fill in their solutions in the code templates.
- The functions written by the students are imported by the evaluation code and scores out of 30 are calculated by each question.
- The scores are then pushed to a Firebase database (if the student wants to) where the judges can track them.

## Questions and Evaluation
- Question 1 and Question 2 are about noise removal. The submissions are evaluated by using Mean Squared Error (mse) score.
- Question 3 is a simplified version of image color segmentation. The submissions are evaluated by using Intersection over Union (IoU) score.
- Question 4 is about histogram equalization. The submissions are evaluated by comparing the difference between the maximum number of pixels for an intensity value to the minimum number of pixels for an intensity value.
- Question 5 deals with counting the number of faces in a given image using any Computer Vision concept. The submissions are evaluated by checking the absolute deviation from the ground truth value.
