def reversebygroups(arr , k):
    i=0 #points to the start of each group
    n = len(arr) #length of the array; total number of elements stored here
    while i < n: #will work until i stays inside the array hence less than n
        left = i #will point to the first element of group
        right = min(i + k-1, n-1) #will point to the last(or third) element of group; since we do not want to go out of the array, we use min
        while left < right: #will swap until we get the middle element
            arr[left], arr[right] = arr[right], arr[left] #now first and last(or third) elements swapped with each other
            left +=1 #left pointer moving
            right -=1 #right pointer moving
        i +=k #will jump to the next group
#User-Input
arr = list(map(int, input("Enter Array: ").split()))
k = int(input("Enter the size of group: "))
reversebygroups(arr , k)
print("Array after reversing by groups: ")
print (*arr)


       #OUTPUT:
#Enter Array: 1 2 3 4 5 6 7 8
#Enter the size of group: 3
#Array after reversing by groups: 
#3 2 1 6 5 4 8 7


