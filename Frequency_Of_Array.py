'''8. Find Frequency of Each Element
👉 Problem: Count how many times each element appears.
✔️ Covers: Traversal, Indexing.
Example:
Input: [1, 2, 2, 3, 1, 4]
Output: 1 → 2 times, 2 → 2 times, 3 → 1 time, 4 → 1 time '''
arr=[1,2,3,3,1,4]
def Frequency(arr):
    freq={}
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq        
freq=Frequency(arr)
print(freq)