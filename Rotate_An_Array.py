'''10. Rotate an Array (Basic)
👉 Problem: Shift elements to the left by 1 position.
✔️ Covers: Indexing, Traversal.
Example:
Input: [1, 2, 3, 4, 5]
Output: [2, 3, 4, 5, 1]  '''

arr=[1,2,3,4,5]
def Rotate_arr(arr):
    for i in range(len(arr)):
        result=arr[1:]+arr[:1]
    return result    
result=Rotate_arr(arr)
print(result)
   
