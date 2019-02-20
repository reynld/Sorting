### helper function
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    a = 0
    b = 0
    # since arrA and arrB already sorted, we only need to compare the first element of each when merging!
    for i in range( 0, elements ):
        if a >= len(arrA):    # all elements in arrA have been merged
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):  # all elements in arrB have been merged
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:  # next element in arrA smaller, so add to final array
            merged_arr[i] = arrA[a]
            a += 1
        else:  # else, next element in arrB must be smaller, so add it to final array
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


### recursive sorting function
def merge_sort(arr):
    # 
    if len( arr ) > 1:
        left = merge_sort( arr[ 0 : len( arr ) // 2 ] )
        right = merge_sort( arr[ len( arr ) // 2 : ] )
        arr = merge( left, right )   # merge() defined later
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# TO-DO: implement the Quick Sort function below USING RECURSION

def get_pivot(arr, low, high):
    mid = (high + low) // 2
    pivot = high
    if arr[low] < arr[mid]:
        if arr[mid] < arr[high]:
            pivot = mid
    elif arr[low] < arr[high]:
        pivot = low

    return pivot

def parition(arr, low, high):
    # get pivot returns the median value in the array
    # out of the lowest middle and higest position
    pivot_index = get_pivot(arr, low, high)

    #gets the value at the index which is our pivot
    pivot_value = arr[pivot_index]

    # swapping the values at the pivot index and the lowest index
    arr[pivot_index], arr[low] = arr[low], arr[pivot_index]

    # assingning the lowest position to a most_left variable
    most_left = low

    # loops through the array range between the lowest position and the highest position
    for i in range (low, high+1):
        # if value at position i is less than the pivot value
        if arr[i] < pivot_value:
            # move the order over to the next position
            most_left += 1
            # swap value at index i and the the value at the new most_left index
            arr[i], arr[most_left] = arr[most_left], arr[i]
    
    # swap value at the lowest position and the value at the most_left position
    arr[low], arr[most_left] = arr[most_left], arr[low]

    # return the left most index where 
    return most_left


def quick_sort( arr, low, high ):
    # arr is the array we are trting to sort
    # low is the lowest position in the array, most left position
    # high is the gihest position in the array, most right position

    # if the lowest position is still less than the highest position
    if low < high:
        # get a pivot to split up the array
        pivot = parition(arr, low, high)
        quick_sort(arr, low, pivot-1)
        quick_sort(arr, pivot + 1, high)

    return arr

# try it out
arr = [2,5,9,7,4,1,3,8,6];
print(arr);
arr = quick_sort(arr, 0, len(arr) - 1);
print(arr);



# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr




# Brady Solution
def partition(arr, low, high):
    pivot = arr[high]

    index = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            index += 1
            arr[index], arr[j] = arr[j], arr[index]
        
    arr[index + 1], arr[high] = arr[high], arr[index + 1]
    return index + 1

def quick_sort(arr, low, high) :
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot -1)
        quick_sort(arr, pivot + 1, high)
    return arr


# Carlos solution
def quick_sort(arr):
        # base case (arrays with 0 or 1 are already sorted)
    if (len(arr) < 2):
        # so just return the array
        return arr
    else:
        # else start your pivot at the first number
        pivot = arr[0]
        # sub array of all the elements less than the pivot
        less = [i for i in arr[1:] if i <= pivot]
        # sub-array of all the elements greater than the pivot
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


