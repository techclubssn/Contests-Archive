import os #line:1
import cv2 #line:2
import sys #line:3
import glob #line:4
import json #line:5
import numpy as np #line:6
from question1 import remove_salt_and_pepper #line:8
from question2 import remove_noise #line:9
from question3 import threshold_red #line:10
from question4 import histogram_equalization #line:11
from question5 import count_people #line:12
import firebase_admin #line:14
from firebase_admin import credentials ,firestore #line:15
def load_dirs (OO0000OOOO0OOO0O0 ):#line:17
    OO00OO0OOOOO0O000 =os .path .join (os .getcwd (),'input','Question '+str (OO0000OOOO0OOO0O0 ))#line:19
    OO000OOO00OOOOOOO =os .path .join (os .getcwd (),'eval','Question '+str (OO0000OOOO0OOO0O0 ))#line:20
    O00OO0OOOOO000O00 =sorted (glob .glob (os .path .join (OO000OOO00OOOOOOO ,'*.txt')))#line:22
    O0OOOO000O00O0OOO =sorted (glob .glob (os .path .join (OO00OO0OOOOO0O000 ,'*.png')))#line:23
    return O00OO0OOOOO000O00 ,O0OOOO000O00O0OOO #line:25
def decode_answer (OOO00O0OOO000OO0O ):#line:27
    O0OOOO0OOOOOOOO0O =lambda OO000O00O0OOO0000 :int (OO000O00O0OOO0000 ,16 )#line:29
    with open (OOO00O0OOO000OO0O ,'r')as O00OOOO00O0OOO00O :#line:31
        O0O0O00OOOOOO00O0 =O00OOOO00O0OOO00O .read ().split ('/')#line:32
        O0OOO000O0OOOO0OO =np .array (list (map (O0OOOO0OOOOOOOO0O ,O0O0O00OOOOOO00O0 [1 :]))).reshape (eval (O0O0O00OOOOOO00O0 [0 ]))#line:33
    return O0OOO000O0OOOO0OO .astype (np .uint8 )#line:35
def evaluate_mse (O0O00O00OOO00O00O ,O0OOO00OO0000000O ):#line:37
    O000O0O0O00O000O0 =255 *255 #line:39
    OOO0OO0000OOO0O0O =np .square (O0O00O00OOO00O00O -O0OOO00OO0000000O ).mean ()#line:40
    O0OOO0O0000O0O0OO =(O000O0O0O00O000O0 -OOO0OO0000OOO0O0O )/O000O0O0O00O000O0 #line:41
    return O0OOO0O0000O0O0OO #line:43
def evaluate_mask (OO0O0O00O000OOO00 ,OO000OOO00000000O ):#line:45
    OOO0O0O0O00O00O0O =np .count_nonzero ((OO0O0O00O000OOO00 +OO000OOO00000000O )==2 )#line:47
    O00O0OO0O000OOOO0 =np .count_nonzero ((OO0O0O00O000OOO00 +OO000OOO00000000O )>=1 )#line:48
    OOO00OOO0OOOOO0O0 =OOO0O0O0O00O00O0O /O00O0OO0O000OOOO0 #line:49
    return OOO00OOO0OOOOO0O0 #line:51
def evaluate_histogram (O00O0O0OO0OOOO000 ,OOOO0O0O00OOOO000 ):#line:53
    OOO000OOO0O0O000O =np .histogram (O00O0O0OO0OOOO000 .ravel ())[0 ]#line:55
    OOO00O0OO0000OOO0 =sum (OOO000OOO0O0O000O .ravel ())#line:56
    OO000O0OOOO0OO000 =OOO000OOO0O0O000O .max ()-OOO000OOO0O0O000O .min ()#line:57
    OOO0O00OOO00OO0O0 =(OOO00O0OO0000OOO0 -OO000O0OOOO0OO000 )/OOO00O0OO0000OOO0 #line:59
    return OOO0O00OOO00OO0O0 #line:61
def evaluate_count (O0OOOOO0000O00OO0 ,OOO0OO0OO00O0OO0O ):#line:63
    OOO00OOOOOO0O0O00 =1 -(abs (O0OOOOO0000O00OO0 -OOO0OO0OO00O0OO0O )/(OOO0OO0OO00O0OO0O +10e-12 ))#line:65
    return OOO00OOOOOO0O0O00 #line:67
def run ():#line:69
    OO0O0O0000O0000O0 ="""
$$$$$$$$\ $$$$$$$$\  $$$$$$\  $$\        $$$$$$\  
\__$$  __|$$  _____|$$  __$$\ $$ |      $$  __$$\ 
   $$ |   $$ |      $$ /  \__|$$ |      $$ /  $$ |
   $$ |   $$$$$\    \$$$$$$\  $$ |      $$$$$$$$ |
   $$ |   $$  __|    \____$$\ $$ |      $$  __$$ |
   $$ |   $$ |      $$\   $$ |$$ |      $$ |  $$ |
   $$ |   $$$$$$$$\ \$$$$$$  |$$$$$$$$\ $$ |  $$ |
   \__|   \________| \______/ \________|\__|  \__|
                                                                                                    
    """#line:82
    print (OO0O0O0000O0000O0 )#line:84
    print ('Welcome to the Tesla Image Processing and Computer Vision contest!')#line:85
    if not os .path .exists (os .path .join (os .getcwd (),'metadata.json')):#line:87
        print ('-----------------------------------------------')#line:88
        print ('Please register before submitting your results.')#line:89
        print ('You can register by running: python register.py')#line:90
        print ('-----------------------------------------------')#line:91
        sys .exit (0 )#line:92
    with open ('metadata.json','r')as OO00OO00O0OOOO000 :#line:94
        OOO0O00OOOOOO0O00 =json .load (OO00OO00O0OOOO000 )#line:95
    print ('----------------------------')#line:98
    print ('Evaluating your submissions:')#line:99
    print ('----------------------------')#line:100
    OOOO0O00O0OOO0O0O =33 #line:102
    O0OOO0OO0O00O0000 =[]#line:104
    O0O0000O0O0O00OOO ,O0OO0OOOO0OO0OO0O =load_dirs (1 )#line:105
    O00O00000OOOO0OO0 =0 #line:106
    for O0OO00OOO0OO00OO0 ,(OO0OOOOOO0O00OO0O ,O00O000OOOOOOO00O )in enumerate (zip (O0OO0OOOO0OO0OO0O ,O0O0000O0O0O00OOO ),1 ):#line:108
        O0OO000OO000O0O0O =decode_answer (O00O000OOOOOOO00O )#line:110
        OOO0O00OOO0OOOOOO =cv2 .imread (OO0OOOOOO0O00OO0O ,1 )#line:111
        try :#line:113
            OOO0O00OOO0OOOOOO =remove_salt_and_pepper (OOO0O00OOO0OOOOOO )#line:114
            OOO0000000OO00OO0 =evaluate_mse (OOO0O00OOO0OOOOOO ,O0OO000OO000O0O0O )#line:115
        except :#line:116
            print ('Looks like something is wrong with Question 1 submission -- Score of 0 is provided for test case '+str (O0OO00OOO0OO00OO0 ))#line:117
            OOO0000000OO00OO0 =0 #line:118
        O00O00000OOOO0OO0 +=OOO0000000OO00OO0 *(1 +(O0OO00OOO0OO00OO0 >3 ))#line:121
    O00O00000OOOO0OO0 =(O00O00000OOOO0OO0 /9 )*30 #line:124
    O0OOO0OO0O00O0000 .append (O00O00000OOOO0OO0 )#line:125
    print ('Question 1:',O00O00000OOOO0OO0 )#line:126
    O0O0000O0O0O00OOO ,O0OO0OOOO0OO0OO0O =load_dirs (2 )#line:128
    O00O00000OOOO0OO0 =0 #line:129
    for O0OO00OOO0OO00OO0 ,(OO0OOOOOO0O00OO0O ,O00O000OOOOOOO00O )in enumerate (zip (O0OO0OOOO0OO0OO0O ,O0O0000O0O0O00OOO ),1 ):#line:131
        O0OO000OO000O0O0O =decode_answer (O00O000OOOOOOO00O )#line:133
        OOO0O00OOO0OOOOOO =cv2 .imread (OO0OOOOOO0O00OO0O ,1 )#line:134
        try :#line:136
            OOO0O00OOO0OOOOOO =remove_noise (OOO0O00OOO0OOOOOO )#line:137
            OOO0000000OO00OO0 =evaluate_mse (OOO0O00OOO0OOOOOO ,O0OO000OO000O0O0O )#line:138
        except :#line:139
            print ('Looks like something is wrong with Question 2 submission -- Score of 0 is provided for test case '+str (O0OO00OOO0OO00OO0 ))#line:140
            OOO0000000OO00OO0 =0 #line:141
        O00O00000OOOO0OO0 +=OOO0000000OO00OO0 *(1 +(O0OO00OOO0OO00OO0 >3 ))#line:144
    O00O00000OOOO0OO0 =(O00O00000OOOO0OO0 /9 )*30 #line:147
    O0OOO0OO0O00O0000 .append (O00O00000OOOO0OO0 )#line:148
    print ('Question 2:',O00O00000OOOO0OO0 )#line:149
    OO0OO000O0OOOO000 =127 #line:151
    O0O0000O0O0O00OOO ,O0OO0OOOO0OO0OO0O =load_dirs (3 )#line:153
    O00O00000OOOO0OO0 =0 #line:154
    for O0OO00OOO0OO00OO0 ,(OO0OOOOOO0O00OO0O ,O00O000OOOOOOO00O )in enumerate (zip (O0OO0OOOO0OO0OO0O ,O0O0000O0O0O00OOO ),1 ):#line:156
        O0OO000OO000O0O0O =cv2 .cvtColor (decode_answer (O00O000OOOOOOO00O ),cv2 .COLOR_BGR2GRAY )#line:158
        O0OO000OO000O0O0O =O0OO000OO000O0O0O /255 #line:159
        OOO0O00OOO0OOOOOO =cv2 .imread (OO0OOOOOO0O00OO0O ,1 )#line:160
        try :#line:162
            OO0000OOOO0OO0000 =threshold_red (OOO0O00OOO0OOOOOO )/255 #line:163
            OOO0000000OO00OO0 =evaluate_mask (OO0000OOOO0OO0000 ,O0OO000OO000O0O0O )#line:164
        except :#line:165
            print ('Looks like something is wrong with Question 3 submission -- Score of 0 is provided for test case '+str (O0OO00OOO0OO00OO0 ))#line:166
            OOO0000000OO00OO0 =0 #line:167
        O00O00000OOOO0OO0 +=OOO0000000OO00OO0 *(1 +(O0OO00OOO0OO00OO0 >3 ))#line:170
    O00O00000OOOO0OO0 =(O00O00000OOOO0OO0 /9 )*30 #line:173
    O0OOO0OO0O00O0000 .append (O00O00000OOOO0OO0 )#line:174
    print ('Question 3:',O00O00000OOOO0OO0 )#line:175
    O0O0000O0O0O00OOO ,O0OO0OOOO0OO0OO0O =load_dirs (4 )#line:177
    O00O00000OOOO0OO0 =0 #line:178
    for O0OO00OOO0OO00OO0 ,(OO0OOOOOO0O00OO0O ,O00O000OOOOOOO00O )in enumerate (zip (O0OO0OOOO0OO0OO0O ,O0O0000O0O0O00OOO ),1 ):#line:180
        O0OO000OO000O0O0O =cv2 .cvtColor (decode_answer (O00O000OOOOOOO00O ),cv2 .COLOR_BGR2GRAY )#line:182
        OOO0O00OOO0OOOOOO =cv2 .imread (OO0OOOOOO0O00OO0O ,0 )#line:183
        try :#line:185
            OOO0O00OOO0OOOOOO =histogram_equalization (OOO0O00OOO0OOOOOO )#line:186
            OOO0000000OO00OO0 =evaluate_histogram (OOO0O00OOO0OOOOOO ,O0OO000OO000O0O0O )#line:187
        except :#line:188
            print ('Looks like something is wrong with Question 4 submission -- Score of 0 is provided for test case '+str (O0OO00OOO0OO00OO0 ))#line:189
            OOO0000000OO00OO0 =0 #line:190
        O00O00000OOOO0OO0 +=OOO0000000OO00OO0 *(1 +(O0OO00OOO0OO00OO0 >3 ))#line:193
    O00O00000OOOO0OO0 =(O00O00000OOOO0OO0 /9 )*30 #line:196
    O0OOO0OO0O00O0000 .append (O00O00000OOOO0OO0 )#line:197
    print ('Question 4:',O00O00000OOOO0OO0 )#line:198
    _OO000O000O0O0O0OO ,O0OO0OOOO0OO0OO0O =load_dirs (5 )#line:200
    O00OO00OOOOO00000 =OOOO0O00O0OOO0O0O +OO0OO000O0OOOO000 +73 #line:202
    with open (os .path .join (os .getcwd (),'eval','Question 5','count.txt'),'r')as OO00OO00O0OOOO000 :#line:204
        O0O00O0O0OO0OOO0O =OO00OO00O0OOOO000 .read ().strip ().split ('/')#line:205
    O00O0O000OO0O00O0 =lambda O00OO0OOO00OO000O :int (O00OO0OOO00OO000O ,16 )-O00OO00OOOOO00000 #line:207
    O0O00O0O0OO0OOO0O =list (map (O00O0O000OO0O00O0 ,O0O00O0O0OO0OOO0O ))#line:208
    O00O00000OOOO0OO0 =0 #line:209
    for O0OO00OOO0OO00OO0 ,(OO0OOOOOO0O00OO0O ,O00O000OOOOOOO00O )in enumerate (zip (O0OO0OOOO0OO0OO0O ,O0O0000O0O0O00OOO ),1 ):#line:211
        O0OO000OO000O0O0O =O0O00O0O0OO0OOO0O [O0OO00OOO0OO00OO0 -1 ]#line:213
        OOO0O00OOO0OOOOOO =cv2 .imread (OO0OOOOOO0O00OO0O ,0 )#line:214
        try :#line:216
            OO000OO00O0O00OOO =count_people (OOO0O00OOO0OOOOOO )#line:217
            OOO0000000OO00OO0 =evaluate_count (OO000OO00O0O00OOO ,O0OO000OO000O0O0O )#line:218
        except :#line:219
            print ('Looks like something is wrong with Question 5 submission -- Score of 0 is provided for test case '+str (O0OO00OOO0OO00OO0 ))#line:220
            OOO0000000OO00OO0 =0 #line:221
        O00O00000OOOO0OO0 +=OOO0000000OO00OO0 *(1 +(O0OO00OOO0OO00OO0 >3 ))#line:224
    O00O00000OOOO0OO0 =(O00O00000OOOO0OO0 /9 )*30 #line:227
    O0OOO0OO0O00O0000 .append (O00O00000OOOO0OO0 )#line:228
    print ('Question 5:',O00O00000OOOO0OO0 )#line:229
    print ('-------------------')#line:231
    print ('Submitting Results:')#line:232
    print ('-------------------')#line:233
    print ('You can submit results any number of times you want to. ')#line:234
    print ('We will only consider the final submission regardless of its score.')#line:235
    OO0000OOO0000OOO0 =input ('Would you like to submit your scores? (Y/N) ')#line:236
    print ('--------------------------------------------')#line:237
    if OO0000OOO0000OOO0 =='y'or OO0000OOO0000OOO0 =='Y':#line:239
        print ('Submitting...')#line:241
        os .environ ['GOOGLE_APPLICATION_CREDENTIALS']='ENTER YOUR GOOGLE CREDS HERE'#line:242
        OO000O00OOO00OOOO =credentials .ApplicationDefault ()#line:243
        firebase_admin .initialize_app (OO000O00OOO00OOOO ,{'projectId':'ENTER YOUR FIREBASE PROJECT ID HERE',})#line:246
        OOOOO00O00O0O00OO =firestore .client ()#line:248
        O0O0O0OOOO0O00OOO =OOOOO00O00O0O00OO .collection ('submissions').document (OOO0O00OOOOOO0O00 ['reg_num'])#line:250
        O0O0O0OOOO0O00OOO .set ({'question1':O0OOO0OO0O00O0000 [0 ],'question2':O0OOO0OO0O00O0000 [1 ],'question3':O0OOO0OO0O00O0000 [2 ],'question4':O0OOO0OO0O00O0000 [3 ],'question5':O0OOO0OO0O00O0000 [4 ],'name':OOO0O00OOOOOO0O00 ['name'],'id':OOO0O00OOOOOO0O00 ['id'],'dept':OOO0O00OOOOOO0O00 ['dept'],'year':OOO0O00OOOOOO0O00 ['year']})#line:261
        print ('Done!')#line:262
    else :#line:264
        print ('Not Submitted.')#line:266
if __name__ =='__main__':#line:268
    run ()