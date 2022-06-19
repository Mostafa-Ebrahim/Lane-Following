import matplotlib.pyplot as plt
from matplotlib.image import imread
import numpy as np

# Read in the image and print out some stats
image = imread('./test.jpg')
print('This image is: ', type(image), 
         'with dimensions:', image.shape)

# Grab the x and y size and make a copy of the image
ysize = image.shape[0]
xsize = image.shape[1]
color_select = np.copy(image)
region_select = np.copy(image)

# Define our color selection criteria
rgb = [200,200,200]

# Identify pixels below the threshold
thresholds = (image[:,:,0] < rgb[0]) | (image[:,:,1] < rgb[1]) | (image[:,:,2] < rgb[2])
color_select[thresholds] = [0,0,0]

# Display the image                 
plt.imshow(color_select)
plt.show()