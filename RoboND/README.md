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

Steps for cluster segmentation have been added to the pcl_callback() function in the template Python script. Not required, but to help your reviewer consider adding screenshots of output at different steps in your writeup with brief explanations.
---

Both compute_color_histograms() and compute_normal_histograms() functions have been filled out and SVM has been trained using train_svm.py. Please provide a snapshot of your normalized confusion matrix (output from train_svm.py in your writeup / README. Object recognition steps have been implemented in the pcl_callback() function within template Python script. Not required, but to help your reviewer consider adding screenshots of output at different steps in your writeup with brief explanations.
---

# Pick and Place Setup

You can add this functionality to your already existing ros node or create a new node that communicates with your perception pipeline to perform sequential object recognition. Save your PickPlace requests into output_1.yaml, output_2.yaml, and output_3.yaml for each scene respectively. Add screenshots in your writeup of output showing label markers in RViz to demonstrate your object recognition success rate in each of the three scenarios. Note: for a passing submission, your pipeline must correctly identify 100% of objects in test1.world, 80% (4/5) in test2.world and 75% (6/8) in test3.world.
