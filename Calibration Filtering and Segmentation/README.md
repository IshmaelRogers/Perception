## Ishmael Rogers
## Robotics Software Engineer, Infinitely Deep Robotics Group,  
## www.idrg.io  
## 2018

[image1]: PinHoleModel
[image2]: LensModel
[image3]: chessboard
[image4]: chessboard_angles
[image5]: corner_found
[link1]: http://wiki.ros.org/image_pipeline
[image6]: voxelDS
[image7]: inliers_outliers


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
Now we explore calibration in ROS's [image_pipeline][link1] which contain a suite of package that provide a variety of image manipulation tools. 
camera_calibration is a package that allows the calibration of Monocular, Stereo and RGB-D cameras

The process involves combining the RGB camera data with accompanying depth camera data to generate 3D point clouds.

# Point Cloud Filtering 
The process of removing usless, excessive and conflicting data points from within a point cloud.
NOTE: Adversarial data might correspond to an object on the ground that resembles a target object on a table which could cause a false positive if it is not filtered out. 

The following are commonly used filters from the Point Cloud Library:

VoxelGrid Downsampling Filter
ExtractIndices Filter
PassThrough Filter
RANSAC Plane Fitting
Outlier Removal Filter


Task: Identifying a an obeject in a cluttered environment. 
---
When observing point cloud data, you may notice that a majority of the data is not useful for identifying desired targets. Things such a background or other objects do not help recognize the target and should be regarded as noise. 
NOTE: Processing this excessive data is inefficient and can cause you to waste compute cycles


## Voxel Grid Downsampling  
Becuase RGB-D cameras provide feature rich and dense point clouds, it is best to downsample the data using a Voxel Grid Downsampling Filter.  

A voxel grid filter allows for the downsampling of data by a spatial average of the points in the cloud confined by each voxel. The sampling size can ve adjusted by setting the voxel size along each dimension. 

![alt text][image6]

A voxel is short for volume element and is the 3D version of the pixels.

We can view the results of the downsampling using pcl_viewer

$ python RANSAC.py
$ pcl_viewer voxel_downsampled.pcd 

NOTE: The voxel size (or leaf size) are measured in meters. Therefore setting it to 1 implies that the voxel is 1 cubic meter in volume
which might not be ideal as it will remove important features. 
NOTE: In practice, it is typically best to start with a small voxel size and then increment to a larger size until a point is reach that any further increase would result in a loss of important features. 
## Pass Through Filter 
Given prior information about the location of the target in the scene, a Pass Through Filter can be applied to remove useless data from your point cloud. 

The Pass Through Filter is similar to a cropping tool, which allows you to crop any given 3D point cloud by specifying an axis with cut-off values along that axis. 

Region of Interest
---
The region that is allow to pass through the filter and remove some excess data.


## Segmentation

In this step we will divide the point cloud data into smaller subsets based on some common property. Moreover, we can seperate the data into meaningful pieces based on shape, color, size or neighborhood. 

NOTE: In our project, the table itself is segmented out

## RANSAC
The Random Sample Consensus algorithm can be used to identify points in the cloud dataset that belong to a particular model.
The model could be a plane, a cylinder, a box or any other common shape.

Ground segmentation is an essential part of a mobile robot's perception toolkit for autonmous navigation. Plane segmentation can be used for collision avoidance with objects and to determine traversable terrain. 

The algorithm assumes that the dataset is composed of both inliers and outliers.

inliers
---
Are defined by a particular model with a specific set of parameters.

outliers
--- 
Are the data points that do not fit that model and can be discarded

![alt text][image7]

In general if there is prior knowledge of a certain shape in a given dataset, RANSAC can be used to estimate what pieces of the point cloud belong to that shape

Disadvantages of RANSAC
---
There is no upper limit on the time it can take to model parameters.
NOTE: This can be helped by choosing a fixed number of iterations. However, if a lower iteration number is chosen, the solution obtained may not be optimal. 

## RANSAC Plane Fitting 

The RANSAC algorithm consist of performing two iteratively repeated steps on a given data set:
0. Hypothesis 
1. Verification.

Hypothesis
---

A hypothetical shape of the model is generated by randomly selecting a minimal subset of n-points and estimating the corresponding shape-model parameters.

A minimal subset contains the smallest number of points required to uniquely estimate a model. 

Example:
---
0. Two points are needed to determine a line
1. Three non-collinear points are needed to determin a plane (see below)

<a href="https://www.codecogs.com/eqnedit.php?latex=p_{1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p_{1}" title="p_{1}" /></a> , <a href="https://www.codecogs.com/eqnedit.php?latex=p_{2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p_{2}" title="p_{2}" /></a> , and <a href="https://www.codecogs.com/eqnedit.php?latex=p_{3}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p_{3}" title="p_{3}" /></a> are three randomly selected non-collinear points. 

<a href="https://www.codecogs.com/eqnedit.php?latex=p_{1}&space;=&space;(x_{1},&space;y_{1},&space;z_{1})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p_{1}&space;=&space;(x_{1},&space;y_{1},&space;z_{1})" title="p_{1} = (x_{1}, y_{1}, z_{1})" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=p_{2}&space;=&space;(x_{2},&space;y_{2},&space;z_{2})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p_{2}&space;=&space;(x_{2},&space;y_{2},&space;z_{2})" title="p_{2} = (x_{2}, y_{2}, z_{2})" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=p_{3}&space;=&space;(x_{3},&space;y_{3},&space;z_{3})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p_{3}&space;=&space;(x_{3},&space;y_{3},&space;z_{3})" title="p_{3} = (x_{3}, y_{3}, z_{3})" /></a>

A plane can be described using the equation:

<a href="https://www.codecogs.com/eqnedit.php?latex=ax&space;&plus;&space;by&space;&plus;cz&space;&plus;&space;d=0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?ax&space;&plus;&space;by&space;&plus;cz&space;&plus;&space;d=0" title="ax + by +cz + d=0" /></a>
The coefficients a, b, c, d can be found by solving the following system of equations:

<a href="https://www.codecogs.com/eqnedit.php?latex=ax_{1}&space;&plus;&space;by_{1}&space;&plus;cz_{1}&space;&plus;&space;d=0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?ax_{1}&space;&plus;&space;by_{1}&space;&plus;cz_{1}&space;&plus;&space;d=0" title="ax_{1} + by_{1} +cz_{1} + d=0" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=ax_{2}&space;&plus;&space;by_{2}&space;&plus;cz_{2}&space;&plus;&space;d=0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?ax_{2}&space;&plus;&space;by_{2}&space;&plus;cz_{2}&space;&plus;&space;d=0" title="ax_{2} + by_{2} +cz_{2} + d=0" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=ax_{3}&space;&plus;&space;by_{3}&space;&plus;cz_{3}&space;&plus;&space;d=0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?ax_{3}&space;&plus;&space;by_{3}&space;&plus;cz_{3}&space;&plus;&space;d=0" title="ax_{3} + by_{3} +cz_{3} + d=0" /></a>

Once a model is established, the remaining points in the point cloud are tested against the resulting candidate shape to determine how many of the points are approximated well by the model. 
NOTE: After a certain number of iterations, the shape that possesses the largest percentage of inliers is extracted and the algorithm continues to process the remaining data. 

## Extracting Indicies

In our example, the RANSAC algorithm identifies which indices in the point cloud correspond to the table. If the Pass Through Filter is applied correctly, then the indices not corresponding to the table are the objects on the table.

The Extract Indicies Filter allows for the extraction of points from a point cloud by providing a list of indices. 

The output of the RANSAC fitting (the inliers) correspond to the point cloud indices that were within max_distance of the best fit model.

The filter does not perform any advanced filtering action therefore it is typically used along with other techniques to obtain a subset of points from an input point cloud.
NOTE: Most object recognition algorithms return a set of indices associated with the points that form the identified object. 

It is convenient to us the Extract Indices Filter to extract the point cloud associated with the identified object. 

Object Extraction
---

Using the Extract Indices helped us to extract the subset of points corresponding to the table itself. In actually we want to completely get rid of the table and focus on the objects on top of the table.
NOTE: To extract all the objects of interest from the point cloud, we can change the negative flag on the extract method to True.

## Outlier Removal Filter

Calibration helps take care of distortion however noise due to external factors like dust in the environment, humidity in the air or light sources can lead to sparse outliers which can corrupt the results further. These outliers can lead to complications in the estimation of point cloud characteristics like curcature, gradients, etc. leading to erroneous values, which might cause failures at different stages in our perception pipeline. 

StatisticalOutlierRemoval filter
--
Uses statistical analysis to remove the outliers that do not meet certain criteria. For each point in the point cloud, it computes the distance to all its neighbors and then calculates a mean distance. 
NOTE:Assuming a Gaussian distribution, all points whose mean distabces are outside of an intercal defined by the global distances mean standard deviation are considered to be outliers and are removed fromt the point cloud.


