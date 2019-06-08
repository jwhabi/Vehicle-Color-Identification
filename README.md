# Vehicle-Color-Identification

***		README	***
***Vehicle Color Identification***
Jaideep Whabi - A20403110 
CS 595 - Deep Learning
																				

Problem Statement
In recent years the number of cars on roads has increased exponentially and, identifying them has
become a very big task. Vehicle color information is one of the 3 important elements in ITS
(Intelligent Traffic System), the other two being– Make and model of the car and license plate
recognition. Vehicle color is an important property for vehicle identification and provides visual
cues for fast action law enforcement. Recognizing the color of a moving or even a still vehicle can
be a very challenging task because of several factors including weather conditions, quality of
video/image acquisition, and strip combination of the vehicle. Different ensemble algorithms can
be used to give us color recognition.

Proposed Solution

Dehazing of images
A major part of this project will deal with the removal of haze from images. This algorithm can be
applied to many other problems too. This algorithm uses atmospheric light to give us clearer
images. As cities grow bigger, we are encountering more air and light pollution. Both contribute
to hazy images that are difficult to process in real time. We will be using transmission maps and
atmospheric light to generate a clear image.

Classifiers
The haze free images are fed to a convolutional network for feature engineering and the output is
fed to a fully connected network for classification. Multiple color spaces (RGB, HSV and
CIE LAB) are tested to determine the color space which is easiest to interpret and leads to higher
performance. The final model, when given an image of a vehicle, will be able to predict the color
of the vehicle with high accuracy.																				

Dataset Used
The Vehicle Color Recognition Dataset contains 15601 vehicle images in eight colors, which are
black, blue, cyan, gray, green, red, white and yellow. The images are taken in the frontal view captured
by a high-definition camera with the resolution of 1920×1080 on the urban road. The collected data
set is very challenging due to the noise caused by illumination variation, haze, and over exposure. The
dataset is available at -
http://122.205.5.5:8071/~pchen/project.html																				

Files included:

1. renamefilestoenglish.py
2. color_recognition-v1.ipnynb
3. haze free images.py
4. Project Report
5. vehicle_color_haze_free_model.h5
6. vehicle_color_model_haze_free_weights.h5
7. Vehicle color identification.pptx

Links included:
1. Original dataset: http://122.205.5.5:8071/~pchen/project.html
2. Processed dataset (haze free images): https://drive.google.com/open?id=1DKYmI1R-3yOYXaE0VYWxypppOUOxnBGx


Instructions:

- If you are using the original dataset, you will have to rename the image files since many of them have non-english characters.
- To rename all files in the dataset, execute the renamefilestoenglish.py file
- In the directory chooser dialog box, browse to the parent directory where the subdirectories are folders of each color and select it.
- Then the code will take care of the rest and give you a dataset where filenames conform to utf-8 encoding.


- The 'haze free images.py' file takes the original dataset as input, and outputs a dataset with haze-free images where color contrasts are clearer.
- Input to this program is the parent directory of the folders of each color of the original dataset which has to be written in the code by editing the string 'your input here'
- Output to this program will be stored in a directory. Prior to executing the program , please create an empty directory structure similar to the original dataset. i.e. 
  create a parent folder and 8 sub-folders with sub-folder names as color names.
- edit the string 'your output here' to the parent directory of the new directory structure you have created.
- The program will then pick up each image from the input directory, treat it hor hazyness, the save the new treated image in the output directory structure.
- This code takes roughly 6-12 hours to execute per color class, therefore it is advised to break your data in batches and execute the code, and also try to execute on multiple machines.
- To treat all 8 classes on 2-3 machines, an approximate ETA will be 24-48 hours.
- ********An copy of the dataset already treated for hazyness (haze free images) can be found here: https://drive.google.com/open?id=1DKYmI1R-3yOYXaE0VYWxypppOUOxnBGx ********
- The classification model is trained on part of this data. You can pick any set of images at random, to test/ explore the model.

- color_recognition-v1.ipnynb is a python notebook file containing the model training and testing code. Data is read in the same way as renamefilestoenglish.py
- The notebook will walk you through data preprocessing and normalization, model training and validation, training the optimal mmodel, testing, and model statistics.

- The 2 '.h5' files are saved instances of the final model and the model weights. You can try and load these files to get a pre-trained model ready for testing.


****NOTE: for any access or execution issues please email jwhabi@hawk.iit.edu ****
Thank you for your time. 

References
1. Reza Fuad Rachmadi: “Vehicle Color Recognition using Convolutional Neural Network”,
2015; [http://arxiv.org/abs/1510.07391 arXiv:1510.07391]
2. K. S. Aarathi and A. Abraham, "Vehicle color recognition using deep learning for hazy
images," 2017 International Conference on Inventive Communication and Computational
Technologies (ICICCT), Coimbatore, 2017
3. C. Hu, X. Bai, L. Qi, P. Chen, G. Xue and L. Mei, "Vehicle Color Recognition With Spatial
Pyramid Deep Learning," in IEEE Transactions on Intelligent Transportation Systems,
vol. 16, no. 5, Oct. 2015
4. K. He. Et al.: Single Image Haze Removal Using Dark Channel Prior. Proceedings of the
2009 IEEE Conference on Computer Vision and Pattern Recognition, 2009
5. J.-W. Hsieh, L.-C. Chen, S.-Y. Chen, D.-Y. Chen, S. Alghyaline, and H.-F. Chiang,
Vehicle Color Classification Under Different Lighting Conditions Through Color
Correction, IEEE Sensors Journal, 2015,
6. P. Chen, X. Bai and W. Liu, Vehicle Color Recognition on an Urban Road by Feature
Context, IEEE Transactions on Intelligent Transportation Systems (TITS), 2014,
7. E. Dule, M. Gokmen, M. S. Beratoglu, A convenient feature vector construction
for vehicle color recognition, Proc. 11th WSEAS International Conference on Neural
Networks, Evolutionary Computing and Fuzzy systems, pp: 250255, (2010)
8. N. Baek, S.-M. Park, K.-J. Kim, and S.-B. Park, Vehicle Color Classification
Based on the Support Vector Machine Method, International Conference on Intelligent
Computing, ICIC 2007
9. J.-W. Son, S.-B. Park, and K.-J. Kim, A convolutional kernel method for color
recognition, International Conference on Advanced Language Processing and Web
Information Technology (ALPIT 2007)
10. http://alexlenail.me/NN-SVG/LeNet.html , Used to create neural network visualizations.
11. Fast Single Image Defogging by Zhiming Tan, Xianghui Bai, Bingrong Wang and Akihiro
Higashi
12. https://www.learnopencv.com/color-spaces-in-opencv-cpp-python/
