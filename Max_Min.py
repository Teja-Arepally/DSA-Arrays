'''3. Find Maximum and Minimum
 Problem: Find the largest and smallest element in an array.
 Covers: Initialization, Indexing.
Example:
Input: [4, 9, 2, 7, 5]
Output: Max = 9, Min = 2 '''

n=[4,9,2,7,5]
max_num=float("-inf")
min_num=float("inf")
def max_min(n,max_num,min_num):
    for i in n:
        if max_num<i:
            max_num=i
    for j in n:
        if min_num>j:
            min_num=j
        
    return max_num,min_num
max_num,min_num=max_min(n,max_num,min_num)
print(f"Maximum number in a given array:{max_num}")
print(f"Maximum number in a given array:{min_num}")