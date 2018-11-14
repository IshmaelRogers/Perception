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

Step 1. cv2.calibrateCamera()
---
Computes the calibration matrices and distortion coefficients 

Step 2. Use cv2.undistort()
---
Undistorts a test image

Intrinsics vs Extrinsics 
---
Intrinsic parameters are things that are inherent to the camera's focal length and optical center as well as the distortion coefficients.
NOTE: These properties remain the same no matter how the camera is positioned in the world.

Extrinsic parameters of the calibration process describe how the camera's reference frame is oriented within the world reference frame. 

## Intrinsic Calibration

Use this to explore the topic of intrinsic calibration more closely. --> https://github.com/udacity/RoboND-Camera-Calibration

Once we have the follwoing, we are ready to perform the intrinsic calibration:
0. Object points
1. Image points 
2. (x,y) shape of the image

In OpenCV we will use the cv2.calibrateCamera() function as seen below:
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, (img.shape[1], img.shape[0]), None, None)
NOTE: The outputs that contain the intrinsic camera matrix and distortion coefficients are:

0. mtx -> intrinsic camera matrix
<a href="https://www.codecogs.com/eqnedit.php?latex=intrinsic\&space;camera\&space;matrix&space;=&space;\begin{bmatrix}&space;f_{x}&space;&0&space;&c_{x}&space;\\&space;0&space;&&space;f_{y}&space;&c_{y}&space;\\&space;0&space;&0&space;&1&space;\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?intrinsic\&space;camera\&space;matrix&space;=&space;\begin{bmatrix}&space;f_{x}&space;&0&space;&c_{x}&space;\\&space;0&space;&&space;f_{y}&space;&c_{y}&space;\\&space;0&space;&0&space;&1&space;\end{bmatrix}" title="intrinsic\ camera\ matrix = \begin{bmatrix} f_{x} &0 &c_{x} \\ 0 & f_{y} &c_{y} \\ 0 &0 &1 \end{bmatrix}" /></a>

Where <a href="https://www.codecogs.com/eqnedit.php?latex=f_{x}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f_{x}" title="f_{x}" /></a> and <a href="https://www.codecogs.com/eqnedit.php?latex=f_{y}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f_{y}" title="f_{y}" /></a> correspond to the focal length. 

<a href="https://www.codecogs.com/eqnedit.php?latex=c_{x}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?c_{x}" title="c_{x}" /></a> and <a href="https://www.codecogs.com/eqnedit.php?latex=c_{y}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?c_{y}" title="c_{y}" /></a> correspond to the camera's optical center in the (x,y) plane. 

1. dist -> distortion cofficients
<a href="https://www.codecogs.com/eqnedit.php?latex=distortion\&space;coefficients&space;=&space;(k_{1},&space;k_{2},&space;p_{1},&space;p_{2},&space;k_{3})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?distortion\&space;coefficients&space;=&space;(k_{1},&space;k_{2},&space;p_{1},&space;p_{2},&space;k_{3})" title="distortion\ coefficients = (k_{1}, k_{2}, p_{1}, p_{2}, k_{3})" /></a>
NOTE: The k's are radial disortion coefficients and p's are tangential distortion coefficients
NOTE: We apply the undist = cv2.undistort(img, mtx, dist, None, mtx) to apply the above equations

Please see cameraCalibration.py to run the code that implements this process.

## Extrinsic Calibration
The relationship between the position of a point in the 2D pixel coordinates and the position of a corresponding point in the 3D world coordinates is defined by the pinhole camera model:

<a href="https://www.codecogs.com/eqnedit.php?latex=z_{c}\begin{bmatrix}&space;u\\&space;v\\&space;1&space;\end{bmatrix}&space;=&space;K[RT]\begin{bmatrix}&space;x_{w}\\&space;y_{w}\\&space;z_{w}\\&space;1&space;\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?z_{c}\begin{bmatrix}&space;u\\&space;v\\&space;1&space;\end{bmatrix}&space;=&space;K[RT]\begin{bmatrix}&space;x_{w}\\&space;y_{w}\\&space;z_{w}\\&space;1&space;\end{bmatrix}" title="z_{c}\begin{bmatrix} u\\ v\\ 1 \end{bmatrix} = K[RT]\begin{bmatrix} x_{w}\\ y_{w}\\ z_{w}\\ 1 \end{bmatrix}" /></a>

Where:

K is the intrinsic matrix derived previously
R and T are the extrinsic parameters which denote the coordinate system transfomations from the 3D world coordinates to 3D camera coordinates
NOTE: the extrinsic parameters define the position of the camera center and the camera's heading in world coordinates.

T is the position of the origin of the world coordinate system expressed in coordinates of the camera-centered coordinate system.

The position of the camera C = -R’ T

NOTE: Given that the extrinsic parameters determine the 3D pose of respective camera in the world coordinates, they can also be used for the process of image registration.

Image registration is the process of transforming the data frame from one camera to match the data frame from another, pixel by pixel.
NOTE: This is essential for the creation of an accurate point cloud.

## RGBD in ROS
Now we explore calibration in ROS's [http://wiki.ros.org/image_pipeline][image_pipeline] 
# Point Cloud Filtering 

## Voxel Grid Downsampling  

## Pass Through Filter 

## Segmentation

## RANSAC

## RANSAC Plane Fitting 

## Extracting Indicies

## Outlier Removal Filter
