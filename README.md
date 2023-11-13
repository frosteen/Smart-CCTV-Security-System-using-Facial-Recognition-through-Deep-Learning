# Smart-CCTV-Security-System-using-Facial-Recognition-through-Deep-Learning
A practice of International Project Design from Chung Yuan Christian University (CYCU), Taoyuan City, Taiwan

For more additional information about the project. Please check <a href="./Smart CCTV Final Paper.pdf">Smart CCTV Final Paper.pdf</a>.

## Awards & Recognition
⭐ Presented in Chung Yuan Christian University (CYCU), Taoyuan City, Taiwan<br>
⭐ Recognized as an Excellent Work - International<br>
⭐ Recognized as an Excellent Work - National<br>

## Requirements
```bash
# Executed on Python3.7.8
PyQt4
cv2
numpy
dlib
face_recognition
PIL
```

## Installation
```bash
pip install -r requirements.txt
```

## Getting Started
1. Run ~data_gathering.py
1. Run ~trainer.py
1. Run Main.py

## Abstract
The project consists of a 720p camera connected to a Raspberry Pi model 3B located at the entrance of a certain location. It is created with a Graphical User Interface (GUI) to show the real-time recording of the camera. It has a feature that indicates when the last (wanted) person was seen in the location of the camera it captures the face, and records a video for a short period of time (9-10 seconds). At the same time it will create logs on a notepad, that indicates who is detected along with the time and date that he/she was last seen, as well as the location. Frontal Face Haar Cascade Algorithm is used for the face detection while deep learning algorithms: Histogram of Oriented Gradients (HOG) and Linear Support Vector Machine (SVM) are used to recognize the face.

## Motivation and Purpose
This smart CCTV project is made for the purpose of security as it detects people’s faces and its location where he/she was last seen. Current commercial CCTVs can only record real-time video of certain places and hasn’t been integrated with facial recognition algorithms yet. Police officers are having a hard time detecting/finding people-of-interest since they’re still doing it manually. This project is also a low-cost implementation of deep learning and facial recognition algorithms through the use of a Raspberry Pi.

## Introduction
In the modern society, people need security everywhere. Every building, houses, streets, and other places need a Closed Circuit TV also known as CCTV  for security purposes. A Closed-Circuit Television, is a TV system in which signals are not publicly distributed but are monitored, primarily for surveillance and security purposes. [1] Facial recognition is also somehow a necessity for a CCTV, wherein the program will detect faces of different people using different algorithms available in modern technology. Facial recognition can help users to identify the person-of-interest. One innovation in today's technology is the deep learning. Deep learning, a subset of machine learning, is an artificial intelligence function that copies the human brain’s workings in data processing, specifically creating patterns for decision making use. [2]

## Innovation Adoption or Practical
With the results observed, this project can help future CCTV industries to improve their products as it is proven that with the help of the microcontroller, the CCTV can refine its capabilities especially in detecting the identities of people. Combining the facial recognition algorithms and deep learning algorithms, it can create a more accurate program that will detect people and its location depending on the camera's placement. Practical applications of this Smart CCTV project includes: detection of wanted criminals roaming around the center of a city, location of professors inside and outside the school building, attendance and location of the students in a particular class, improved household CCTV that can detect the location of the family members around the house, and many more.

## Conclusion and Recommendations
Facial recognition integrated with deep learning outcomes great improvement in modern technology. The image processing algorithms present in the program were accurate enough to detect real life persons even if its trained images in the database are in the form of pictures; in this project, it’s in the form of miniature pictures. It was observed that the program can detect registered faces immediately, and can also detect the registered images even in a different background with different lighting conditions. It can be said that the Haar Cascade Algorithm and the Histogram of Oriented Gradients (HOG) Algorithm were effective algorithms that allowed the system to detect and recognize faces. Although, it was observed that with only one Raspberry Pi model B, it can only handle a single camera with its processing power, but overall it does its job and the system works smoothly. 

In sum, the study was successful and was able to function the way it was expected to. Yet, the researchers recommend others whom might continue this project, to improve the system by adding more cameras to the system. This is to ensure that the system to be more effective once applied in a real situation. Also, for them to remember that when adding another or more cameras, the processing power of the microcontroller must be improved as well. The researchers suggest to try clustering multiple Raspberry Pis, and make use of: parallel computing, multiprocessing, or multi threading. Also, by trying the latest model of the Raspberry Pi which is Raspberry Pi model 3B+, this will theoretically help the system to handle more processes at a single period of time.

## Contributors
* Luis Daniel Pambid
* Carl Francis John Reyes
* Aivje Tribiana
* Ian Chen
* Chi-An Li
* Yuya Tagaya
* Imam Jurjawi

## References
[1] CCTV (closed circuit television). Retrieved from https://whatis.techtarget.com/definition/CCTV-closed-circuit-television<br>
[2] Deep Learning. Retrieved from https://www.investopedia.com/terms/d/deep-learning.asp<br>
[3] Digital Signal Processing. Retrieved from https://en.wikipedia.org/wiki/Digital_image_processing<br>
[4] Facial Recognition. Retrieved from https://www.techopedia.com/definition/32071/facial-recognition<br>
[5] Deep Learning Haar Cascade Explained. Retrieved from http://www.willberger.org/cascade-haar-explained/<br>
[6] Histogram of Oriented Gradients (HOG) Descriptor. Retrieved from https://software.intel.com/en-us/ipp-dev-reference-histogram-of-oriented-gradients-hog-descriptor<br>
[a] Support Vector Machines(SVM). Retrieved from https://towardsdatascience.com/https-medium-com-pupalerushikesh-svm-f4b42800e989.<br>
[7] About OpenCv. Retrieved from https://opencv.org/about/<br>
[8] PyQt4 Project Description. Retrieved from https://pypi.org/project/PyQt4/<br>
[9] dlib C++ Library. Retrieved from http://dlib.net/<br>
[10] PIL documentation. Retrieved from https://pillow.readthedocs.io/en/stable/<br>
[11] Numpy. Retrieved from https://www.numpy.org/<br>
[12] The world's simplest facial recognition api for Python and the command line. Retrieved from https://github.com/ageitgey/face_recognition<br>

## Tip
**If you liked our hard work, I would really appreciate if you can buy some coffee for us.**

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/frosteen)