# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for x in range(cur_index, len(arr)):
            if arr[x] < arr[smallest_index]:
                smallest_index = x



        # TO-DO: swap
        num_smallest = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = num_smallest




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # you have a list of numbers that needs to be arranged in order
    # [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
    # create a for loop to loop through the array
    # compare each number inside the list and see if the number needs to be sorted
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]




    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr