###################################
Constructing Histograms
###################################


import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

#plot the image

image=mpimg.imread('Filename.jpeg')

plt.imshow(image)

###############( Construct RGB Histogram )#########################################
def color_hist(img, nbins=32, bins_range=(0,256)):
	r_hist=np.histogram(image[:, :, 0], bins=32, bins_range=(0,256))
	g_hist=np.histogram(image[:, :, 1], bins=32, bins_range=(0,256))
	b_hist=np.histogram(image[:, :, 2], bins=32, bins_range=(0,256))

	hist_features = np.concatenate((r_hist[0], g_hist[0], b_hist[0])).astype(np.float64)
	norm_features = hist_features / np.sum(hist_features)
	
	return norm_features


#################################################################################

########################### PLOTTING HISTOGRAMS#######################
#Generate bin centers

bin_edges = r_hist[1]
bin_centers = (bin_edges[1:] + bin_edges[0:len(bin_edges)-1])/2


#Plot three bar charts
fig = plt.figure(figsize=(12,3))
plt.subplot(131)
plt.bar(bin_centers, r_hist[0])
plt.xlim(0,256)
plt.title('R Histogram')
plt.subplot(132)
plt.bar(bin_centers, g_hist[0])
plt.xlim(0, 256)
plt.title('G Histogram')
plt.subplot(133)
plt.bar(bin_centers, b_hist[0])
plt.xlim(0, 256)
plt.title('B Histogram')
plt.show()
####################################################################################

#####################( Construct HSV Histogram )#####################################

def color_hist(img, nbins=32, bins_range=(0,256)):
	hsv_img = cv2.cvtcolor(img, cv2.COLOR-RGB2HSV)
	h_hist=np.histogram(image[:, :, 0], bins=32, bins_range=(0,256))
	s_hist=np.histogram(image[:, :, 1], bins=32, bins_range=(0,256))
	v_hist=np.histogram(image[:, :, 2], bins=32, bins_range=(0,256))

	hist_features = np.concatenate((h_hist[0], s_hist[0], v_hist[0])).astype(np.float64)
	norm_features = hist_features / np.sum(hist_features)
	
	return norm_features

##############################################################################################

#####################################( Plotting HSV Histograms) ##############################
feature_vec=color_hist(img, nbins=32, bins_range=(0,256)):
	
if feature_vec is not None:
	fig = plt.figure(figsize=(12,6))
	plt.plot(feature_vec)
	plt.title('HSV Feature Vector', fontsize=30)
	plt.tick_params(axis = 'both', which = 'major', labelsize=20)
	fig.tight_layout()
else:
	print('Function is returning none....') 
