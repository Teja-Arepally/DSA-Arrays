'''7. Copy One Array to Another
👉 Problem: Copy all elements from one array to another.
✔️ Covers: Traversal, Indexing.
Example:
Input: [1, 2, 3]
Output: Copied Array = [1, 2, 3]  '''

arr=[1,2,3]
copied_arr=[]
def Copying_array(arr,copied_arr):
    for i in arr:
        copied_arr.append(i)
    return copied_arr
copied_arr=Copying_array(arr,copied_arr)
print(f'Copying of array:{copied_arr}')