def dnf(arr,n):
    low = 0
    high = n-1
    mid = low
    while (mid<=high):
        if arr[mid] == 0:
            arr[mid],arr[low] = arr[low],arr[mid]
            low+=1
            mid+=1
        elif arr[mid] == 1:

            mid+=1
        else:
            arr[mid],arr[high] = arr[high],arr[mid]
            high-=1
    return arr


arr = [0,1,1,2,1,0,2]
print(dnf(arr,len(arr)))
