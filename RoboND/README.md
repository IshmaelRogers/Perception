## Ishmael Rogers 
## Robotics Software Engineer, Infinitely Deep Research Group
## www.idrg.io
## Udacity Perception Project
## 2018

pcl_callback() Function
---
This function will be called each time a message is publish to the "/pr2/world/points topic. It consist of the entire perception pipeline (i.e segmentation, clustering and object recognition). It also calls the pr2 mover function that tells the robot how to pick and place the object of interest. 

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
        

Both compute_color_histograms() and compute_normal_histograms() functions have been filled out and SVM has been trained using train_svm.py. Please provide a snapshot of your normalized confusion matrix (output from train_svm.py in your writeup / README. Object recognition steps have been implemented in the pcl_callback() function within template Python script. Not required, but to help your reviewer consider adding screenshots of output at different steps in your writeup with brief explanations.
---

# Pick and Place Setup

You can add this functionality to your already existing ros node or create a new node that communicates with your perception pipeline to perform sequential object recognition. Save your PickPlace requests into output_1.yaml, output_2.yaml, and output_3.yaml for each scene respectively. Add screenshots in your writeup of output showing label markers in RViz to demonstrate your object recognition success rate in each of the three scenarios. Note: for a passing submission, your pipeline must correctly identify 100% of objects in test1.world, 80% (4/5) in test2.world and 75% (6/8) in test3.world.
