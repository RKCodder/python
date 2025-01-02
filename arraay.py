# from array import array
# arr=array("i",[12,34,56,34])
# print(arr)
# arr.append(10)
# print(arr)
#arr.reverse()
#print(arr)
# for trv in arr:  for traversing 
    # print(trv)
# print(arr[0])
# i=0
# while(i<len(arr)):
#     print(arr[i])
#     i=+1

# print(arr.count(34)) count the number of occurence means how many time elements comes in arry 
# print(arr.pop()) delete the last elements from the arry 

from numpy import *
a=array([1,23,4434,])
print(a)
a[2]=300 # update the element by using indexing 
print(a)

# arr = array([[1, 2, 3], [4, 5, 6]]) # 2d arry 
# print(arr)
# print(arr[0, 1]) # row 0 column 1



# In Python, arrays (or lists) support operations like **reverse**, **push**, **pop**, and more. If you're using **NumPy**, these methods may behave differently, or you might need equivalent NumPy operations. Here's a breakdown of such methods for both **native Python lists** and **NumPy arrays**:

# ---

# ### 1. **For Native Python Lists**

# #### **Reverse**
# Reverses the order of the elements in the list.

# ```python
# arr = [1, 2, 3, 4, 5]
# arr.reverse()  # In-place reversal
# print(arr)  # [5, 4, 3, 2, 1]
# ```

# Alternatively:
# ```python
# reversed_arr = arr[::-1]  # Creates a new reversed list
# ```

# #### **Push**
# Python lists use `append()` to add an element to the end.

# ```python
# arr = [1, 2, 3]
# arr.append(4)
# print(arr)  # [1, 2, 3, 4]
# ```

# #### **Pop**
# Removes and returns the last element (or an element at a specific index).

# ```python
# arr = [1, 2, 3]
# last_element = arr.pop()  # Removes the last element
# print(last_element)  # 3
# print(arr)  # [1, 2]

# # Pop at a specific index
# element = arr.pop(0)  # Removes the first element
# print(element)  # 1
# print(arr)  # [2]
# ```

# #### **Insert**
# Adds an element at a specific index.

# ```python
# arr = [1, 3, 4]
# arr.insert(1, 2)  # Insert 2 at index 1
# print(arr)  # [1, 2, 3, 4]
# ```

# #### **Remove**
# Removes the first occurrence of a specific value.

# ```python
# arr = [1, 2, 3, 2]
# arr.remove(2)  # Removes the first 2
# print(arr)  # [1, 3, 2]
# ```

# #### **Sort**
# Sorts the list in ascending order (in-place).

# ```python
# arr = [3, 1, 4, 2]
# arr.sort()  # [1, 2, 3, 4]

# # Sort in descending order
# arr.sort(reverse=True)  # [4, 3, 2, 1]
# ```

# ---

# ### 2. **For NumPy Arrays**

# #### **Reverse**
# Use slicing to reverse a NumPy array.

# ```python
# import numpy as np

# arr = np.array([1, 2, 3, 4, 5])
# reversed_arr = arr[::-1]
# print(reversed_arr)  # [5, 4, 3, 2, 1]
# ```

# #### **Push (Append)**
# Use `np.append()` to add elements to an array. Note that this creates a new array (NumPy arrays are immutable in size).

# ```python
# arr = np.array([1, 2, 3])
# new_arr = np.append(arr, 4)
# print(new_arr)  # [1, 2, 3, 4]
# ```

# #### **Pop**
# NumPy does not have a direct `pop()` method. You can remove elements by slicing or using `np.delete()`.

# ```python
# arr = np.array([1, 2, 3, 4])
# new_arr = np.delete(arr, -1)  # Remove the last element
# print(new_arr)  # [1, 2, 3]
# ```

# #### **Insert**
# Use `np.insert()` to insert elements at a specific index.

# ```python
# arr = np.array([1, 3, 4])
# new_arr = np.insert(arr, 1, 2)  # Insert 2 at index 1
# print(new_arr)  # [1, 2, 3, 4]
# ```

# #### **Remove**
# Use `np.delete()` to remove elements by index.

# ```python
# arr = np.array([1, 2, 3, 2])
# new_arr = np.delete(arr, np.where(arr == 2)[0][0])  # Remove the first occurrence of 2
# print(new_arr)  # [1, 3, 2]
# ```

# #### **Sort**
# Use `np.sort()` to sort the array.

# ```python
# arr = np.array([3, 1, 4, 2])
# sorted_arr = np.sort(arr)
# print(sorted_arr)  # [1, 2, 3, 4]

# # Sort in descending order
# sorted_arr_desc = np.sort(arr)[::-1]
# print(sorted_arr_desc)  # [4, 3, 2, 1]
# ```

# ---

# Let me know if you'd like further clarification or help with a specific operation!