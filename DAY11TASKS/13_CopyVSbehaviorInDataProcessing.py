import numpy as np
arr=np.array([10,20,30,40])
copy_arr=arr.copy()
arr[0]=99
print(arr)
print(copy_arr)
arr2=np.array(arr)
view_arr=arr2.view()
arr2[0]=99
print(view_arr)
