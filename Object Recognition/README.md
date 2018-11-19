# Ishmael Rogers
# Robotics Software Engineer, Infinitely Deep Robotics Group
# www.idrg.io 
# Atlanta, Ga
# 2018 

# Object Recognition

[image1]: ./images/RGBD.PNG
[image2]: ./images/HSV.PNG

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

HSV is very robust to lighting changes 

![alt text][image2]

# HSV Intuition

# Color Histograms

# Surface Normals

# Support Vector Machine 

# Support Vector Machine Intuition

# Support Vector Machine Image Classification 

# Recognition Exercise

# Generate Features

# Train the Support Vector Machine

# Improving the Model

# Object Recognition
