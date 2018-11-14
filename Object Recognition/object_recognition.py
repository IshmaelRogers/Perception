#######Object Recognition###########


# add the following to the pcl_callback() function 

#########

# classify the clusters

detected_objects_labels = []
detect_objects = []

for index, pts_list in enumerate(cluster_indices):

#grab the points for the cluster from the extracted outliers 

	pcl_cluster = cloud_objects.extract(pts_list)
	
	#TODO: convert cluster from pcl to ROS using helper function
	
	#Extract histogram features 
	
	#refer to capture_features.py

	#Make predictions, retrieve the label for the result
	#add it to detected_objects_labels list
	
	prediction = clf.predict(scaler.transform(feature.reshape(1,-1)))
	
	label = encoder.inverse_transform(predicitio)[0]
	detected_objects_labels.append(label)

	#publish a label to RViz
	
	label_pos = list(white_cloud[pts_list[0]]) 
	label_pos += 0.4
	object_markers_pub.publish(make_label(label, label_pos, index))

	#Add the detected object to the list of detected objecs 
	
	do = DetectedObject()
	do.label = label 
	do.cloud = ros_cluster
	detected_objects.append(do_

rospy.loginfo('Detected {} objects: {}'.format(len(detected_objects_labels), detected_objects_labels))

#publish the list of detected objects
	
detected_objects_pub.publish(detected_objects)

# TODO: Create two publishers

#object_markers_pub publishes to ---> /object_markers (message type Marker)

#detected_objects_pub publishes to ---> /detected_objects (message type DetectedObjectsArray\

#Load model 

model = pickle.load(open('model.sav', 'rb'))
clf = model['classifier']
encoder = LabelEncoder()
encoder.classes_ = model['classes']
scaler = model[scaler']
	
