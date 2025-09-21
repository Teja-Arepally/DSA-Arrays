'''6. Count Even and Odd Numbers
 Problem: Count how many even and odd numbers are in the array.
 Covers: Looping, Conditions.
Example:
Input: [1, 2, 3, 4, 5, 6]
Output: Even = 3, Odd = 3 '''

arr=[1,2,3,4,5,6,7,9,10]
Even_count=0
Odd_count=0
def Even_Odd(arr,Even_count,Odd_count):
    for i in arr:
        if(i%2==0):
            Even_count+=1
        else:
            Odd_count+=1
    return Even_count,Odd_count
Even_count,Odd_count=Even_Odd(arr,Even_count,Odd_count)
print(f"Even number in a given array:{Even_count}")
print(f"Odd number in a given array:{Odd_count}")