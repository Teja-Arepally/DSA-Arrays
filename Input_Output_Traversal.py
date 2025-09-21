'''1. Input/Output & Traversal
Problem: Take n integers from the user and print them.
Covers: Input, Output, Traversal.
Example:
Input: 5 → 10 20 30 40 50
Output: 10 20 30 40 50 '''


'''n=int(input("Enter a number:"))
arr=[]
for i in range(n):
    val=int(input(f"Enter a number {i+1}:"))
    arr.append(val)
print("Array elements are:",arr)   '''  


print("By using functions")
def input_array(n):
    arr=[]
    for i in range(n):
        val=int(input(f"Enter a number {i+1}:"))
        arr.append(val)
    return arr
n=int(input("Enter a number:"))
arr=input_array(n)
print("Array elements are:",arr)    