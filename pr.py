"""#bubble sort
arr = [5,1,4,2]

for i in range(len(arr)):

    for j in range(len(arr)-1):

        if arr[j] > arr[j+1]:

            arr[j], arr[j+1] = arr[j+1], arr[j]
            print("change",arr)

print(arr)

#insertion sort
arr = [5,1,4,2]

for i in range(1, len(arr)):

    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:

        arr[j+1] = arr[j]
        j -= 1

    arr[j+1] = key
    print("change",arr)

print(arr)

#selection sort 
arr = [5,1,4,2]

for i in range(len(arr)):

    min_index = i

    for j in range(i+1, len(arr)):

        if arr[j] < arr[min_index]:
            min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]
    print("change",arr)

print(arr)

#merge sort
def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    print("left=",left)
    print("right=",right)

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:

            result.append(left[i])
            i += 1
            print("result with left=",result)

        else:

            result.append(right[j])
            j += 1
            print("result with right=",result)

    result.extend(left[i:])
    result.extend(right[j:])

    return result


arr = [5,2,4,1]

print(merge_sort(arr))



#Counting sort
def counting_sort(arr):

    maximum = max(arr)

    count = [0] * (maximum + 1)

    for num in arr:
        count[num] += 1

    result = []

    for i in range(len(count)):
        print(count[i])

        while count[i] > 0:

            result.append(i)
            print(result)
            count[i] -= 1

    return result


arr = [4,2,2,8,3,3,1]

print(counting_sort(arr))
"""