# Divide and Conquer algorithem

def mergeSort(arr):
    if(len(arr)>1):
        rightarr =arr[:len(arr)//2]
        leftarr = arr[len(arr)//2:]
        mergeSort(rightarr)
        mergeSort(leftarr)
    
        i = 0 #for left array index
        j = 0 #for right array index
        k = 0 #for merged array index
    
        while i < len(leftarr) and j < len(rightarr):
            if(leftarr[i]<rightarr[j]):
                arr[k] = leftarr[i]
                i+=1
            else:
                arr[k] = rightarr[j]
                j+=1
            k+=1
        
        while i <len(leftarr):
            arr[k]= leftarr[i]
            i+=1
            k+=1
        while j < len(rightarr):
            arr[k]=rightarr[j]
            j+=1
            k+=1
        
        
arr = [34,76,23,98,45,87,22,88,33]
mergeSort(arr)
print("merge Sort",arr)