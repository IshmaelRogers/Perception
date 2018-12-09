## Ishmael Rogers 
## Robotics Software Engineer, Infinitely Deep Research Group
## www.idrg.io
## Udacity Perception Project
## 2018

[image1]: ./images/normalized_confusion_matrix.png
[image2]: ./images/out1.png
[image3]: ./images/out2.png
[image4]: ./images/out3.png 


pcl_callback() Function
---
This function will be called each time a message is publish to the "/pr2/world/points topic. It consist of the entire perception pipeline (i.e segmentation, clustering and object recognition). It also calls the pr2 mover function that tells the robot how to pick and place the object of interest. 

Point Cloud Filtering
---
The process of removing useless, excessive and conflicting data points from within a point cloud. NOTE: Adversarial data might correspond to an object on the ground that resembles a target object on a table which could cause a false positive if it is not filtered out.
The following filters were used  from the Point Cloud Library:
VoxelGrid Downsampling Filter ExtractIndices Filter PassThrough Filter RANSAC Plane Fitting Outlier Removal Filter

Voxel Downsampling
---
Becuase RGB-D cameras provide feature rich and dense point clouds, it is best to downsample the data using a Voxel Grid Downsampling Filter.
A voxel grid filter allows for the downsampling of data by a spatial average of the points in the cloud confined by each voxel. The sampling size can ve adjusted by setting the voxel size along each dimension.

Passthrough Filter 
---
Given prior information about the location of the target in the scene, a Pass Through Filter can be applied to remove useless data from your point cloud.
The Pass Through Filter is similar to a cropping tool, which allows you to crop any given 3D point cloud by specifying an axis with cut-off values along that axis.

Segmentaion
---
In this step we will divide the point cloud data into smaller subsets based on some common property. Moreover, we can separate the data into meaningful pieces based on shape, color, size or neighborhood.


RANSAC
---
The Random Sample Consensus algorithm can be used to identify points in the cloud dataset that belong to a particular model. The model could be a plane, a cylinder, a box or any other common shape. The algorithm assumes that the dataset is composed of both inliers and outliers

Inliers
---
The set of points that are defined by a particular model with a specific set of parameters.

Ouliers
---
Are the data points that do not fit that model and can be discarded

Cluster Segmentation
--- 
Is the process of finding similarities among individual points in some point cloud data so that they may be segmented. By clustering data we provide our robot with a way to determine which components of a dataset naturally belong together. NOTE: Clustering can be performed based on spatial neighborhood as well as color.

This clustering algorithm is an alternative to k-means when the number of clusters to expect in the dataset is unknown but something about how the points should be clustered in terms of density (distance between points in a cluster). 

It works by creating clusters by grouping data points that are within some threshold distance, <a href="https://www.codecogs.com/eqnedit.php?latex=d_{th}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?d_{th}" title="d_{th}" /></a> from the nearest other point in the data. 

The decision of whether to place a point in a cluster is based on the Euclidean distance between that point and other cluster members

NOTE: The Euclidean distance is the length of a line connecting two points. The coordniates defining the positions of points in the dataset do no need to be spatial coordinates. 

Given points p and q in an n-dimensional dataset where the position of p and q are defined as follows: 

<a href="https://www.codecogs.com/eqnedit.php?latex=(p_{1},&space;p_{2},\cdots,&space;p_{n})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?(p_{1},&space;p_{2},\cdots,&space;p_{n})" title="(p_{1}, p_{2},\cdots, p_{n})" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=(q_{1},&space;q_{2},\cdots,&space;q_{n})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?(q_{1},&space;q_{2},\cdots,&space;q_{n})" title="(q_{1}, q_{2},\cdots, q_{n})" /></a>

The distance between the two point is:

<a href="https://www.codecogs.com/eqnedit.php?latex=D&space;=&space;\sqrt{(p_{1}-q_{1})^{2}&space;&plus;&space;(p_{2}-q_{2})^{2}&plus;\cdots&space;&plus;&space;(p_{n}-q_{n})^2)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?D&space;=&space;\sqrt{(p_{1}-q_{1})^{2}&space;&plus;&space;(p_{2}-q_{2})^{2}&plus;\cdots&space;&plus;&space;(p_{n}-q_{n})^2)}" title="D = \sqrt{(p_{1}-q_{1})^{2} + (p_{2}-q_{2})^{2}+\cdots + (p_{n}-q_{n})^2)}" /></a>

Steps for DBSCAN Clustering
--
Given a set P of n data points <a href="https://www.codecogs.com/eqnedit.php?latex=p_{1},&space;p_{2},&space;\cdots&space;,&space;p_{n}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p_{1},&space;p_{2},&space;\cdots&space;,&space;p_{n}" title="p_{1}, p_{2}, \cdots , p_{n}" /></a> : 

0. Set contrainsts for the minimum number of points that make up a cluster (min_samples)
1. Set the distance maximum distance between cluster points (max_dist)
2. For ever point <a href="https://www.codecogs.com/eqnedit.php?latex=p_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p_{i}" title="p_{i}" /></a> in P:
      if <a href="https://www.codecogs.com/eqnedit.php?latex=p_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p_{i}" title="p_{i}" /></a> has at least one neighbor within max_dist:
            if <a href="https://www.codecogs.com/eqnedit.php?latex=p_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p_{i}" title="p_{i}" /></a>'s neighbor is part of a cluster 
                  add <a href="https://www.codecogs.com/eqnedit.php?latex=p_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p_{i}" title="p_{i}" /></a> to that cluster
            if <a href="https://www.codecogs.com/eqnedit.php?latex=p_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p_{i}" title="p_{i}" /></a> has at least min_samples -1 neighbors within max_dist:
                  <a href="https://www.codecogs.com/eqnedit.php?latex=p_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p_{i}" title="p_{i}" /></a> becomes a "core member" of the cluster
            else: 
            <a href="https://www.codecogs.com/eqnedit.php?latex=p_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p_{i}" title="p_{i}" /></a> becomes an "edge member" of the cluster
     else:
            <a href="https://www.codecogs.com/eqnedit.php?latex=p_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p_{i}" title="p_{i}" /></a> is defined as an outlier.
        

 compute_color_histograms()
 ---
 The compute_color_histograms() function takes advantage of color information about the objects and computes a histogram in the HSV color space. It normalizeed the results and returns a feature vector. 
 
 compute_normal_histograms()
 ---
 The compute_normal_histograms() function is similar to the above function except that it takes advantage of shape information. 
 
 Normalized confusion matrix 
 ---
 
 ![alt text][image1] 
 
Output Results 
---
Output 1

![alt text][image2]

Output 2 

![alt text][image3] 

Output 3

![alt text][image4]




