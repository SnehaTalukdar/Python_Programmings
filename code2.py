#Python program to find the third largest number in an array 

def findThirdlargest(arr):
    n = len(arr)
    arr.sort() #ascending order

    #checking for third largest number
    for i in range(n-3, -1, -1):

        #Checking so that the number is not the first largest one
        if arr[i] != arr[n-1]:
            return arr[i]
    
#Main Block
if __name__ == "__main__":
    n = int(input("Total Numbers In The Array: "))
arr = list(map(int, input("Enter The Array: ").split()))
print (findThirdlargest(arr))


     #OUTPUT:
#Total Numbers In The Array: 6
#Enter The Array: 1  28 900 34 6 0
#28


    
