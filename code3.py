def reverse_array(arr):
    n = len(arr) #for the length of the array
    temp = [0]*n #for the temporary array
    for i in range(n):
        temp[i] = arr[n-i-1] #for taking out numbers from the end part of the user-given array and put in that temporary array
    for i in range(n):
        arr[i] = temp[i] #pasting temporary array numbers into the original array for printing the desired result

#Main
arr = list(map(int, input("Enter Array: ").split()))
reverse_array(arr)
print("Reversed Array: ") #printing the reversed form of the array
for i in arr:
    print(i, end = " ")


       #OUTPUT
#Enter Array: 1 2 3 4 5 6 7
# #Reversed Array: 
#7 6 5 4 3 2 1 




