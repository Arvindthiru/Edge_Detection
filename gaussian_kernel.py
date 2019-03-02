import numpy as np

def get_gauss_kernel(size=3,sigma=1):
    center=0;
    kernel=np.zeros((size,size))
    for i in range(size):
       for j in range(size):
          diff=np.sqrt((i-center)**2+(j-center)**2)
          kernel[i,j]=np.exp(-(diff**2)/2*sigma**2)
    return kernel/np.sum(kernel)


print(get_gauss_kernel());