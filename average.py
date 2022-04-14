import numpy as np
import math
from decimal import Decimal

# we are using here images with same height and width. So, here image_dimension = n if image is of nxn dims.
# Total_vectors is a list of no of vectors having same Euclidean distances from 'I' vector.
# Total_distances is another list containing the total distance for group of vectors having same distance (accordance with the list 'Distances')
#      so, the length of these two lists are same.
def averagedist(image_dimension):
    no_of_pixels=int(image_dimension*image_dimension)
    m=np.int((no_of_pixels/2) + 1)
    Total_distances=[]
    Total_vectors=[]
    for i in range(m):
        vect=(math.comb(np.int(no_of_pixels/2),i))**2
        dist=round(np.sqrt(2*i), 1)
        app=round(vect * dist ,3)
        Total_distances.append(app)
        Total_vectors.append(vect)
    return Decimal(round(sum(Total_distances)/sum(Total_vectors),3))

print(averagedist(2000))

