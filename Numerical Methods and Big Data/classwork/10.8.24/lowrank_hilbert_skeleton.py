import numpy as np
import matplotlib.pyplot as plt
from skimage import io

# Read image into Python
img=io.imread("hilbert.jpg", as_gray=True)

# Plot image
plt.imshow(img,cmap=plt.cm.gray)
plt.show()

# Change the type of image to double precision
hilbert=np.double(img)

# Compute SVD of image matrix
U,S,VT=np.linalg.svd(hilbert,full_matrices=False)
print(U.shape)
print(S.shape)
print(VT.shape)

# Plot singular values
plt.plot(S)
plt.ylabel('Singular Value \sigma_i')
plt.xlabel('i')
plt.title('Singular Values')
plt.show()

# Make diagonal matrix containing singular values
##############################
#your code goes here

#sigma = np.diag(S)
##############################

# Generate approximate matrices using the principal components
##############################
#your code goes here

rank1= U[:, :1] @ np.diag(S[:1]) @ VT[:1, :]
rank2= U[:, :2] @ np.diag(S[:2]) @ VT[:2, :]
rank5= U[:, :5] @ np.diag(S[:5]) @ VT[:5, :]
rank20= U[:, :20] @ np.diag(S[:20]) @ VT[:20, :]
##############################



# Plot principal component approximations

plt.imshow(rank1,cmap=plt.cm.gray)
plt.title('Rank 1')
plt.show()

plt.imshow(rank2,cmap=plt.cm.gray)
plt.title('Rank 2')
plt.show()

plt.imshow(rank5,cmap=plt.cm.gray)
plt.title('Rank 5')
plt.show()

plt.imshow(rank20,cmap=plt.cm.gray)
plt.title('Rank 20')
plt.show()
