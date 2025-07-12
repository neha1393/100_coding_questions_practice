def find_min(arr,n):
    if n==1:
        return arr[0]
    else:
        return min(arr[n-1],find_min(arr,n-1))
arr=list(map(int,input("enter array elements :").split()))
n=len(arr)
print("the smallest number in the array is ",find_min(arr,n))   
    