

def bubbleSort(arr):
     
    n = len(arr)
 
    # For loop to traverse through all
    # element in an array
    for i in range(n):
        for j in range(0, n - i - 1):
             
            # Range of the array is from 0 to n-i-1
            # Swap the elements if the element found
            #is greater than the adjacent element
            if arr[j].arrival_time > arr[j + 1].arrival_time:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def trashDuplicates(arr):
    new_arr = arr
    
    print(len(arr))
    for i in range(len(arr)-1, 0, -1):
        print(i)
        if arr[i] == arr[i - 1]:
            del new_arr[i]
    return new_arr

    
def groupData(arr):
    #TODO
