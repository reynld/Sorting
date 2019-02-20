# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # fins next smallest element after that element
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        # swap that with current element
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
        # temp = arr[i]
        # arr[i] = arr[smallest_index]
        # arr[smallest_index] = temp

    # For each element in the array, find the next smallest element and swap it
    return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort(arr):

    for x in range(1, len(arr)):
        index = x
        # value we are usign to compare
        value = arr[x]

        #if we are not at position 0 
        # and the value is less than the value to its left
        while index > 0 and arr[index - 1] > value:
            # shift the value on the left one position to the right
            arr[index] = arr[index-1]
            index = index-1
        # assign the valaue to its new position 
        # where it is less than the value positioned on its right
        arr[index]=value
    return arr

# try it out
arr = [2,5,9,7,4,1,3,8,6];
print(arr);
arr = insertion_sort( arr );
print(arr);


# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):
    is_sorted = False
    while not is_sorted:
        is_sorted = True

        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr