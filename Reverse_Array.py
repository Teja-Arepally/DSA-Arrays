'''5. Reverse an Array
👉 Problem: Print the array in reverse order.
✔️ Covers: Indexing, Traversal in reverse.
Example:
Input: [10, 20, 30, 40]
Output: [40, 30, 20, 10]  '''


arr=[10,20,30,40]
rev=[]
def reverse_arr(arr,rev):
    for i in range(len(arr)-1,-1,-1):
        rev.append(arr[i])
    return rev
rev=reverse_arr(arr,rev)
print(f'Reversed array is:{rev}')