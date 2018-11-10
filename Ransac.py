#Import PCL 

import pcl 

#load Point Cloud File 

cloud = pcl.load_XYZRGB('filename.pcd')

#Voxel Grid filter

#a VoxelGrid filter object for the input cloud

vox = cloud.make_voxel_grid_filter()

########################################
#Tune Voxel Parameters

#voxel size
n = 0.01
leaf_size = n 

########################################

#set the voxel with the assigned leaf_size 

vox.set_leaf_size(leaf_size, leaf_size, leaf_size)

#call filter function to obtain the resultant downsampled point cloud

cloud_filtered = vox.filter()

filename = 'voxel_downsampled.pcd'
pcl.save(cloud_filtered, filename)


###################################
#PassThrough filter

#passthrough filter object

passthrough = cloud_filtered.make_passthrough_filter() 

# assign an axis to the pass through filter

filter_axis = 'z'
passthrough.set_filter_field_name(filter_axis)
#############################################
#Tune passthrough parameters
n= 
m=
axis_min = n
axis_max = m 

#############################################
#assign range to the pass through filter

passthrough.set_filter_limits(axis_min, axis_max)

#filter function is used to obtain the resultant point cloud

cloud_filtered = passthrough.filter() 
filename = 'pass_through_filter.pcd'
pcd.save(cloud_filtered, filename)


#RANSAC plane segmentation 

#Segmentation object 

seg = cloud_filtered.make_sementer()

#Set the model to fit 

seg.set_model_type(pcl.SACMODEL_PLANE)
seg.set_method_type(pcl.SAC_RANSAC)

#########################################
# Tune MAX distance parameter 

max_distance = 0.01
seg.set_distance_threshold(max_distance)

#Segment function to obtain a set of inliers indices and model coefficients

inliers, coefficients = seg.segment() 

#Extract Inliers 

extracted_inliers = cloud_filter.extract(inliers, negative=False) 

#Save output point cloud data 

filename = 'extracted_inliers.pcd'
pcl.save(extracted_inliers, filename)



#Extract outliers

#Object extraction step

extracted_outliers = cloud_filtered.extract(inliers, negative = True) 

#####OUTLIER REMOVAL FILTER##############


# Much like the previous filters, we start by creating a filter object: 
outlier_filter = cloud_filtered.make_statistical_outlier_filter()

# Set the number of neighboring points to analyze for any given point
outlier_filter.set_mean_k(50)

# Set threshold scale factor
x = 1.0

# Any point with a mean distance larger than global (mean distance+x*std_dev) will be considered outlier
outlier_filter.set_std_dev_mul_thresh(x)

# Finally call the filter function for magic
cloud_filtered = outlier_filter.filter() 


#Save pcd for cloud
filename = 'extracted_outliers.pcd'
pcl.save(extracted_outliers, filename)

#extract outliers

#Save pcd for tabletop objects
