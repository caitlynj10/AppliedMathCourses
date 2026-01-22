import matplotlib.pyplot as plt
from skimage import io
import numpy as np
from glob import glob

## Code snippets you'll need in no particular order

#right-hand sides
#1) np.linalg.svd(X,full_matrices=0)
#2) U[:,i]
#3) np.mean(trainingFaces,axis=1)[:,np.newaxis]

# Identify naming pattern of files to be read into Python from glob import glob
dir = 'C:/Users/caitlyn jones/OneDrive/classes/math/numerical methods/homework 5/question 1/facedata/facedata/training'
pgm_files = glob(f'{dir}/*.pgm')


    
# Compute number of image files
M = len(pgm_files)

# Compute size of image files
img=io.imread(pgm_files[0], as_gray=True)
m,n = img.shape

# Initialize matrix whose columns correspond to individual images
trainingFaces = np.zeros((m*n,M))

# Initialize matrix whose tiles correspond to individual images
allPersons = np.zeros((m*int(np.sqrt(M)),n*int(np.sqrt(M))))
count = 0

# Open figure window where you will display the images
fig1 = plt.figure()

# Loop over all image files
for i in range(0,M):

    # Acquire the filename of image i
    filename = pgm_files[i]

    # Read image i into Python as a 64 x 64 matrix
    img=io.imread(filename, as_gray=True)

    trainingFaces[:,i] = img.flatten()

    j = int(count % np.sqrt(M))
    k = int((count-count % np.sqrt(M))/np.sqrt(M))
    allPersons[k*m : (k+1)*m,j*n : (j+1)*n] = img
    count += 1

plt.imshow(allPersons,cmap=plt.cm.gray)
plt.show()

#-------- your code begins here--
avgFace = np.mean(trainingFaces,axis=1)[:,np.newaxis]
#-------- your code ends here----

plt.imshow(np.reshape(avgFace,(m,n)),cmap=plt.cm.gray)
plt.show()

# Compute eigenfaces on mean-subtracted training data
print("shape is",avgFace.shape)
print("tile is",np.tile(avgFace,(1,M)).shape)
print("tile is",trainingFaces.shape)
X = trainingFaces - np.tile(avgFace,(1,M))

#-------- your code begins here--
U, S, VT = np.linalg.svd(X,full_matrices=0)
#-------- your code ends here--

coeff = U.T @ X

'''
Transform image into eigenface basis
'''
new_face = io.imread(pgm_files[17], as_gray = True)
new_eigenface = new_face.flatten()[:, np.newaxis]
new_eigenface = new_eigenface - avgFace



new_eigenface_coeff = U.T @ new_eigenface
euc_dis = np.linalg.norm(coeff - new_eigenface_coeff, axis=0)
best_face_match = np.argmin(euc_dis)
matched_image = trainingFaces[:, best_face_match].reshape((m,n))
plt.imshow(matched_image, cmap= "gray")
plt.show()


# Initialize matrix whose tiles correspond to eigenFaces
eigenFaces = np.zeros((m*int(np.sqrt(M)),n*int(np.sqrt(M))))
count = 0

# Loop over all image files
for i in range(0,M):

    # Take ith left singular vector
    #-------- your code begins here--
    img = U[:,i]
    #-------- your code ends here----

    j = int(count % np.sqrt(M))
    k = int((count-count % np.sqrt(M))/np.sqrt(M))
    eigenFaces[k*m : (k+1)*m,j*n : (j+1)*n] = np.reshape(img,(m,n))
    count += 1

plt.imshow(eigenFaces,cmap=plt.cm.gray)
plt.show()


'''
Load Clint Eastwood picture
'''
dir = 'C:/Users/caitlyn jones/OneDrive/classes/math/numerical methods/homework 5/question 1/facedata/facedata/test'
clint_eastwood = io.imread(f'{dir}/Clint_Eastwood_0005.pgm')
plt.imshow(clint_eastwood, cmap = "gray")
plt.show()

'''
Transform and plot the Clint Eastwood eigenface basis
'''
clint_eastwood_eigen = clint_eastwood.flatten()[:, np.newaxis]
clint_eastwood_eigen = clint_eastwood_eigen - avgFace
plt.imshow(clint_eastwood_eigen.reshape((64,64)), cmap="gray")
plt.show()

'''
Compute the Euclidean distance between Clint Eastwood and 
each of the 25 images. Find the best match!
'''

clint_eastwood_coeff = U.T @ clint_eastwood_eigen

euc_dis_clint = np.linalg.norm(coeff - clint_eastwood_coeff, axis=0)
best_face_match = np.argmin(euc_dis_clint)
clint_matched = trainingFaces[:, best_face_match].reshape((m,n))
plt.imshow(clint_matched, cmap= "gray")
plt.show()

