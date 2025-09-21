'''4. Search an Element
👉 Problem: Take an element x and check if it exists in the array.
✔️ Covers: Traversal, Conditionals.
Example:
Input: arr = [1, 4, 6, 8], x = 6
Output: Found '''


arr=[1,4,6,8]
x=6
def search(arr,x):
    for i in arr:
        if x==i:
            return "Found"
    return "Not Found"
result=search(arr,x)    
print(result)            
    