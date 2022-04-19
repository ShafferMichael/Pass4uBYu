# I took this from the class lecture/discussion slides and coded it in python
def heapify(arr, length, i):
    maximum = i  # Initialize maximum as root
    left = 2 * i + 1  # left = 2*i + 1
    right = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if left < length and arr[i] < arr[left]:
        maximum = left

    # if right exists and is greater than current maximum then right is the new maximum
    if right < length and arr[maximum] < arr[right]:
        maximum = right

    # if maximum doesn't equal curr index then swap
    if maximum != i:
        arr[i], arr[maximum] = arr[maximum], arr[i]

        # recursively heapify the root.
        heapify(arr, length, maximum)


# The main function to sort an array of given size
def heap_sort(arr):
    length = len(arr)

    # Build heap(rearrange array)
    # same as for (int i = n / 2 - 1; i >= 0; i--)
    for i in range(length // 2 - 1, -1, -1):
        heapify(arr, length, i)

    # iterate through to extract elements
    for i in range(length - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap - position current root to end
        heapify(arr, i, 0)  # max heapify on the reduced heap
