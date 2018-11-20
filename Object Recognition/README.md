# Ishmael Rogers
# Robotics Software Engineer, Infinitely Deep Robotics Group
# www.idrg.io 
# Atlanta, Ga
# 2018 

# Object Recognition

[image1]: ./images/RGBD.PNG
[image2]: ./images/HSV.PNG
[image3]: ./images/SVM.PNG

Object recognition is a very important concept in computer vision and robotics. We can equip robots with sensors so that they may be able to perceive the world around them. It is our job to provide them with the ability to recoginize objects based on previous data. 

The problem we need to solve is, how can we give the robot the abilty to recognize an object in a scene regardless of its postion and orientation?
The solution is to identify the features that best describe the object we are looking for.
NOTE: The better our description of the object we are looking for, the more likely our algorithm is able to find it. 

# Features

Features are the defining characteristics of an object that help tell it apart from other objects. For our perception algorithm is is just as importatn to identify features we not interested in as well. Once we have an explictly defined set of feeatures, we can train a classifier to recognize the object of interest from the point cloud data. 

What makes a good set of features?
---
A good combination of color and shape data will differnetiate the object of interest from other objects in the scene. The rest of this document highlights how color and shape information can be used to generate a set of features for object recognition. 

# Feature Intuition

Given a segmented point cloud, the following features are useful for identifying a particular object in a scene:

0. Color
1. Position within the scene 
2. Shape
3. Size

The following is a list of features and the characteristics they capture about an object in a point cloud

Object and shape - The color distribution of points in 2D 
Detailed color information - The distribution in color space (e.g., a histogram of each color channel)
Detailed shape information - 3D spatial distribution of points.

# Color Spaces

Each image has an associated red, green and blue color value. RGB can be thought of as the filling of a color grid where the position along each axis defines how much red, green and blue there is in a point 

![alt text][image1] 

An RGB representation of color is good at reproducing what we see with human eyes. However, it is not optimal for representing color in perception tasks dealing with robotics.
NOTE: Objects can appear to have a different colors under various lighting conditions. 

To better optimize our perception pipeline, we convert this RGB color representation to another color representation in order to make thresholding or color selection operations less sensitive to light. 

The Hue Saturationa and Value color space is very robust to lighting changes. Color is represented by a cylinder as seen below.

![alt text][image2]

Hue - The angular position around the cylinder that describes colors in a pixel. 
Saturation - The radial distance from the center axes describing the intensity of that color
Value - The aural brightness lies along the vertical axis. 

Convert RGB to HSV using openCV
---
hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV) 

NOTE: Dim lighting will make the HSV color space more bright. 

# Color Histograms
Previously we mentioned using color information as a way to recognize features of an object of interest. To do this, we make use of histograms. 

Creating histograms involves dividing the the range of data values (0-255) into discrete bins and count up how many of the values fall into each bin. 

Then we compare the colored histogram of a known object image with regions of a test image. We observed that locations with similar color distrubutions will reveal a close match.
NOTE: This method removes any dependence on spatial structure. Therefore, the systen is no longer sensitive to a perfect arrangemenet of points.

Objects with slightly different poses and orientations can still be matched. Size variations in images can be accounted for by normalizing the histograms. 
NOTE: Only using histograms will make us rely solely on the distribution of color value which could lead the system to match unwanted regions and producing false positives. 

See the histograms.py file in this repo in order to find python code for creating histograms. 

# Surface Normals

In this section will learn how to include shape information into our feature set so that we can take advantage of geometric properties in order to properly recoginize objects in a scene. 

The goal is to compare the distribution of points in a point cloud with a reference distribution in order to determine whether or not the object of interest has been found. To caputre shape information, the surface normal distribution is necessary.
NOTE: Histograms will be created using surface normals 

Definition: Normals
---
The normal to any surface is simply a unit vector that is perpendicular to that surface. The normals at different points along a changing surface will point in different directions and the distribution of surface normals taken as a whole can be used to describe the shape of an object. 


# Support Vector Machine 

The SVM is a supervised machine learning algorithm that characterizes the parameter space of a dataset into discrete classes. They work by applying an iterative method to a trainning datasete where each item in the training set is characterized by a feature vector and a label. 

![alt text][image3]

In the image above, each point is characterized by 2 features, A and B. The color of each point corresponds to its label  i.e which class of objeect it represents in the dataset. 

Decision Boundariess
--
The divisions between classes in parameter space.
NOTE: They are shown here by the colored polygons overlaid on the data. 

Creating decision boundaries means that the system is considering a new object for which there is a feature but no label. Doing this can immediately assign it to a specific class. 

NOTE: Once the SVM is trained, it can be used for object recognition.

SVMs in Scikit-Learn
---
Provides a variety of SVM implementations to choose from. In this repo we will use a basic SVM witha linear kernel because it does a good job at classification and it runs faster than more complicated implementations. 

Training Data
---
Before training SVMs we need a labeled data set. 

Please see the SVM.py file in this repo for implementation of SVM's using 

# Support Vector Machine Intuition

Evaluating sk.learn.SVC function
---

0. When clusters slightly overlap the SVC finds a boundary line that best separates the clusters
1. When clusters are completely overlapping the SVC does a poor job of separating them or fails completely 
2. Poly, sigmoid, precomputed and callable kernels are also available besides linear and rbf.

# Support Vector Machine Image Classification 

When using point cloud data, the system will have access to a rich feature set including color and surface normal hostograms. Classification with a 3D point cloud works the same way as with 2 features. Let's explore an example of image classification using color histograms. 

Example
---

This dataset is composed of hundreds of images of cars and other images that might be in the same scene witha car, but they are not cars.
Goal: Train an SVM to recognize whether an image contains a car or not based on an input feature vector composed of color histograms. 
NOTE: Concepts related to training data and evaluating the classifer's performance will be discussed.

General Steps:
---
0. Read in images of both cars and non-cars
1. Extract the color feature for each and scale the feature vectors to zero mean an unit variance.
2. Define a labels vector, shuffle and split data into training and testing sets
3. Define a classifier and train it. 

The labels vector, y will be a binary vector indicating whether each featur vector in the dataset corresponds to a car or non-car
NOTE: 1's will be assigned to cars and 0's will be assigned to non-cars

The function extract_features calls on the histogram function function defined in histogram.py and will generate a list of features from the image dataset.

Given lists of car and non-car features we can define a labels vector that consists of a bunch of ones and zeros




# Recognition Exercise

# Generate Features

# Train the Support Vector Machine

# Improving the Model

# Object Recognition
