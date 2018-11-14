## Ishmael Rogers
## Robotics Software Engineer, Infinitely Deep Robotics Group,  
## www.idrg.io  
## 2018

[image1]: PinHoleModel


# Calibration 

The process of comparing two measurements, ground truth vs sensor readings, and adjusting certain parameters so that the readings match closely. 

Sensors
---
Measure physically quantities directly or indirectly. In practice measurements can be inconsistent due to distortion and noise. Filtering techniques help rectify this noise but removing systematic inconsistentices require an understanding of their root causes.

Temperature, weather and humidity can affect some sensor readings, therefore care needs to be taken when chosing the appropriate sensor for the application. 

Camera calibration is the process of measuring the important charateristics of a camera to understand how the 3D world gets mapped into a 2D image.  


# RGB Camera Model 

Combines the pinhole camera model with the lens model. Both models have a certain distortion associated with it and we will discuss below how to account for these distortions. 

Pinhole camera model
---
![alt text][image1]

Similar to how eyes focusing light reflected off 3d objects in the world and forms upside down and reversed 2D image

The mathematics behind this transformation from 3D to 2D is performed by a Camera Matrix (C) 

Lens camera model
---

In general there are two types of distortions that we would like to correct: Radial and tangential 

Radial
---
<a href="https://www.codecogs.com/eqnedit.php?latex=x_{corrected}=&space;x(1&space;&plus;k_{1}r^{2}&space;&plus;k_{2}r^{4}&space;&plus;k_{3}r^{6})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{corrected}=&space;x(1&space;&plus;k_{1}r^{2}&space;&plus;k_{2}r^{4}&space;&plus;k_{3}r^{6})" title="x_{corrected}= x(1 +k_{1}r^{2} +k_{2}r^{4} +k_{3}r^{6})" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=y_{corrected}=&space;y(1&space;&plus;k_{1}r^{2}&space;&plus;k_{2}r^{4}&space;&plus;k_{3}r^{6})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?y_{corrected}=&space;y(1&space;&plus;k_{1}r^{2}&space;&plus;k_{2}r^{4}&space;&plus;k_{3}r^{6})" title="y_{corrected}= y(1 +k_{1}r^{2} +k_{2}r^{4} +k_{3}r^{6})" /></a>



## Calibration Pattern 

## Extrinsic Calibration

## RGBD in ROS

# Point Cloud Filtering 

## Voxel Grid Downsampling  

## Pass Through Filter 

## Segmentation

## RANSAC

## RANSAC Plane Fitting 

## Extracting Indicies

## Outlier Removal Filter
