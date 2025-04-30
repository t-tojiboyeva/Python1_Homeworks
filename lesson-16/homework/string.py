import numpy as np
#Original List: [12.23, 13.32, 100, 36.32] One-dimensional NumPy array: [ 12.23 13.32 100. 36.32]
arr=np.array([12.23, 13.32, 100, 36.32])
arr
#. Create 3x3 Matrix (2?10)
#Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

#Expected Output:

#[[ 2 3 4] [ 5 6 7] [ 8 9 10]]
import numpy as np
matrix=np.arange(2,11).reshape(3,3)
matrix


#3. Null Vector (10) & Update Sixth Value
#Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.

#[ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

#Update sixth value to 11 [ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]
import numpy as np
vector=np.zeros(10)
print('original vector:',vector)
vector[5]=11
print('updated vector is:',vector)

import numpy as np
arr=np.arange(12,39)
arr
import numpy as np
arr1=np.array([1,2,3,4])
float_arr=arr1.astype(float)
print(arr1)
print(float_arr)
import numpy as np
centigrade=np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])
print('centigrade values are:',centigrade)
farenheit=(centigrade*9/5)+32
farenheit=np.round(farenheit,2)
np.set_printoptions(suppress=True)
print('values in farenheit degrees are:',farenheit)
new_arr=np.array([10,20,30,40])
new_values=[40,50,60,70,80]
updated_arr=np.append(new_arr,new_values)
print(updated_arr)
import numpy as np


arr = np.random.rand(10)
print("Random array:", arr)


mean_val = np.mean(arr)
median_val = np.median(arr)
std_dev = np.std(arr)


print("Mean:", round(np.mean(arr), 2))
print("Median:", round(np.median(arr), 2))
print("std:", round(np.std(arr), 2))

import numpy as np


arr = np.random.rand(10, 10)


min_val = np.min(arr)
max_val = np.max(arr)

print("Random 10x10 array:\n", arr)
print("Minimum value:", min_val)
print("Maximum value:", max_val)

import numpy as np


arr = np.random.rand(3, 3, 3)

print("3x3x3 random array:\n", arr)
