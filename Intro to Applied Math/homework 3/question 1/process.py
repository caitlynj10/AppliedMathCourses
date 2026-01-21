import numpy as np
from skimage import io, color, morphology
import matplotlib.pyplot as plt
import skimage as ski

def position_averages(image):
    ball_position = np.argwhere(image)
    M = np.sum(ball_position)
    x = np.sum(ball_position[:,0])/M
    y = np.sum(ball_position[:,1])/M
    
    return x,y



def process_image(image):
    a = io.imread(image)
    a = ski.img_as_float64(a)
    a/=255.
    
    if a.shape[-1] == 4:
      
       a = a[:, :, :3]
   
    hsv_image = color.rgb2hsv(a)
    blue_upper = 0.55
    blue_lower = 0.62
    
    isolate = (hsv_image[:, :, 0] >= blue_upper) & (hsv_image[:, :, 0] <= blue_lower)
     
    grayscale = np.where(isolate, 1, 0)
    
    denoised = morphology.remove_small_objects(grayscale.astype(bool), min_size=1000)
    
    #print(position_averages(denoised))
    
    #plt.figure()
    #plt.imshow(denoised, cmap = "gray")






ruler = io.imread("drop1.png")
plt.figure()
plt.grid()
plt.imshow(ruler, cmap = "gray")
    
'''   
for k in range(1,8):
    process_image("drop%d.png" %(k))
    plt.pause(0.1)
'''

