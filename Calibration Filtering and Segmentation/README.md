## Ishmael Rogers
## Robotics Software Engineer, Infinitely Deep Robotics Group,  
## www.idrg.io  
## 2018

[image1]: PinHoleModel
[image2]: LensModel
[image3]: chessboard
[image4]: chessboard_angles
[image5]: corner_found


# Calibration 

The process of comparing two measurements, ground truth vs sensor readings, and adjusting certain parameters so that the readings match closely. 

Sensors
---
Measure physically quantities directly or indirectly. In practice measurements can be inconsistent due to distortion and noise. Filtering techniques help rectify this noise but removing systematic inconsistentices require an understanding of their root causes.

Temperature, weather and humidity can affect some sensor readings, therefore care needs to be taken when chosing the appropriate sensor for the application. 

Camera calibration is the process of measuring the important charateristics of a camera to understand how the 3D world gets mapped into a 2D image.  


# RGB Camera Model 

Combines the pinhole camera model with the lens model. Both models have distortion coefficients with them:

<a href="https://www.codecogs.com/eqnedit.php?latex=(k_{1},&space;k_{2},&space;k_{3},&space;p_{1},&space;p_{2})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?(k_{1},&space;k_{2},&space;k_{3},&space;p_{1},&space;p_{2})" title="(k_{1}, k_{2}, k_{3}, p_{1}, p_{2})" /></a>

We will discuss below how to measure and account for these distortions. 

Pinhole camera model
---
![alt text][image1]

Similar to how eyes focusing light reflected off 3d objects in the world and forms upside down and reversed 2D image

The mathematics behind this transformation from 3D to 2D is performed by a Camera Matrix (C) 

Lens camera model
---
![alt text][image2]

Use lenses to focus multiple light rays which allow them to form images quickly. 
NOTE: Bending of light rays can distort images that make lights or shapes appear wide or stretched near the edge of an image.

In general there are two types of distortions that we would like to correct: Radial and tangential 

Radial
---
The effects of radial distortion are minimal at the center of an image and increase radially towards the edges of the image. 

The following equations are used to correct the effects of radial distortion. 
<a href="https://www.codecogs.com/eqnedit.php?latex=x_{corrected}=&space;x(1&space;&plus;k_{1}r^{2}&space;&plus;k_{2}r^{4}&space;&plus;k_{3}r^{6})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{corrected}=&space;x(1&space;&plus;k_{1}r^{2}&space;&plus;k_{2}r^{4}&space;&plus;k_{3}r^{6})" title="x_{corrected}= x(1 +k_{1}r^{2} +k_{2}r^{4} +k_{3}r^{6})" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=y_{corrected}=&space;y(1&space;&plus;k_{1}r^{2}&space;&plus;k_{2}r^{4}&space;&plus;k_{3}r^{6})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?y_{corrected}=&space;y(1&space;&plus;k_{1}r^{2}&space;&plus;k_{2}r^{4}&space;&plus;k_{3}r^{6})" title="y_{corrected}= y(1 +k_{1}r^{2} +k_{2}r^{4} +k_{3}r^{6})" /></a>

Tangential 
---
Occurs when a camera's lens is not aligned perfectly parallel to the imaging plane but the camera film or sensor is. This cause the camera to create an image that appears tilted resulting in images that appear farther away or closer than they actually are. 

The following equations are used to correct tangetial distortion.

<a href="https://www.codecogs.com/eqnedit.php?latex=x_{corrected}=&space;x&space;&plus;&space;[2p_{1}xy&space;&plus;&space;p_{2}(r^{2}&space;&plus;2x^{2})]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{corrected}=&space;x&space;&plus;&space;[2p_{1}xy&space;&plus;&space;p_{2}(r^{2}&space;&plus;2x^{2})]" title="x_{corrected}= x + [2p_{1}xy + p_{2}(r^{2} +2x^{2})]" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=y_{corrected}=&space;y&space;&plus;&space;[p_{1}(r^{2}&space;&plus;2y^{2})&plus;2p_{2}xy]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?y_{corrected}=&space;y&space;&plus;&space;[p_{1}(r^{2}&space;&plus;2y^{2})&plus;2p_{2}xy]" title="y_{corrected}= y + [p_{1}(r^{2} +2y^{2})+2p_{2}xy]" /></a>

## Calibration Pattern 

In order to calibrate a camera a measurement of how 3D points in the world get mapped down onto the 2D image plane of a camera. To do this we will take advantage of OpenCV tools. 

Step 0. Choose a calibration pattern
---
The choice of pattern is arbitrary. The primary goal is to provide a known geometry to take pictures of using the camera. This known geometry will serve as a reference when mapping 3D world points to 2D image points.

![alt text][image3]

Step 1. Take pictures of the test pattern
---

Print the test pattern and take pictures of it from different angles. 

![alt text][image4]

NOTE: Take carefull note of the size of each square. The ones featured above was measured to be 10 cm x 10 cm 

Step 2. Find corners 
---
In this step we will use two OpenCV functions to automatically find and draw the inner corners on the images of the chessboard patter: 

findChessboardCorners()
drawChessboardCorners()

Please see findCorners.py for python code that implements these two functions.

The reult from this function is: 

![alt text][image5]

OpenCV Camera Calibration
---
General steps:

Step 0. cv2.findChessboardCorners() 
--
Finds corners in chessboard images and combines arrays of 2D image points and 3D object points

Step 1. cv2.calibratCamera()
---
Computes the calibration matrices and distortion coefficients 

Step 2. Use cv2.undistort()
---
Undistorts a test image

Intrinsics vs Extrinsics 
---
Intrinsic parameters are things that are inherent to the camera's focal length and optical center as well as the distortion coefficients.
NOTE: These properties remain the same no matter how the camera is positioned in the world.

Extrinsic parameters of the calibration process describe how the cam

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
