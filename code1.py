#Python program to find the second largest number in an array

def findSecondlargest (arr):
    n= len(arr)
    arr.sort() #in-built python function, which sorts all the elements inside the array into ascending order
    
    #Searching for the second largest number
    for i in range(n-2, -1, -1):
        #checking that number is not equal to the first largest number in the array
        if arr[i] != arr[n-1]:
            return arr[i]
    
#Main block
if __name__ == "__main__":
    n = int(input("Total Numbers for Array: "))
    arr = list(map(int, input ("Enter the array: ").split()))
    print(findSecondlargest(arr))
    
    
    #OUTPUT:
#Total Numbers for Array: 6
#Enter the array: 1 2 6 0 0 3
#3
    
    

