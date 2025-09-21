'''2. Sum of Array Elements
 Problem: Find the sum of all elements in an array.
 Covers: Traversal, Indexing.
Example:
Input: [1, 2, 3, 4, 5]
Output: 15 '''

arr=[]
sum_arr=0
def arr_elements(n,arr,sum_arr):
    for i in range(n):
        val=int(input(f"Enter number:{i+1}:"))
        arr.append(val)
    for j in arr:
        sum_arr+=j
    return arr,sum_arr   
n=int(input("Enter elements:"))  
arr,sum_arr = arr_elements(n, arr, sum_arr)
print(f"Array elements are:{arr}")
print(f"Sum of array elements is:{sum_arr}")
