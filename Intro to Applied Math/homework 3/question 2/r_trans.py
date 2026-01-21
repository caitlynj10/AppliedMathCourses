import numpy as np
import matplotlib.pyplot as plt

from skimage.io import imread
from skimage import data_dir
from skimage.transform import radon,iradon,rescale

# Black image with white square
image=np.zeros((200,200))
image[50:100,50:100]=1.0

image_circle = np.zeros((200,200))
center = (100,100)
radius = 25

for i in range(image_circle.shape[0]):
    for j in range(image_circle.shape[1]):
        if np.sqrt((i - center[0])**2 + (j - center[1])**2) < radius:
            image_circle[i, j] = 1.0

plt.title("Original Image with White Circle")
plt.imshow(image_circle, cmap=plt.cm.Greys_r, vmin=0, vmax=1)
plt.show()


# Construct a range of ten angles
theta=np.linspace(0.,360.,360,endpoint=True)

# Carry out the radon tranform
sinogram=radon(image_circle,theta=theta,circle=False)


plt.figure()
plt.plot(sinogram[:,0], color="blue", label="Projection 1 (0 degrees)")
plt.plot(sinogram[:,1], color="red", label="Projection 2 (40 degrees)")
plt.legend()
plt.show()


'''
#Plot the image
plt.title("Original")
plt.imshow(image,cmap=plt.cm.Greys_r,vmin=0,vmax=1)
plt.show()
'''

'''
# Construct a range of ten angles
theta=np.linspace(0.,360.,360,endpoint=True)

# Carry out the radon tranform
sinogram=radon(image,theta=theta,circle=False)


plt.figure()
plt.plot(sinogram[:,0], color="blue", label="Projection 1 (0 degrees)")
plt.plot(sinogram[:,1], color="red", label="Projection 2 (40 degrees)")
plt.legend()
plt.show()



# Print the dimensions of the sinogram
print ("Size of sinogram:",sinogram.shape)


inv_r=iradon(sinogram ,theta=theta)
plt.imshow(inv_r ,cmap=plt.cm.Greys_r ,vmin=0,vmax=1)
plt.show()
'''