def bubble_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len-1):
        flag = 0
        for j in range(0, arr_len-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                flag = 1
                if flag == 0:
                    break
    return arr

arr = [5, 3, 4, 1, 2, 10, 83, 86, 83, 76, 64, 52, 64, 86]
print("List sorted with bubble sort in ascending order: ", bubble_sort(arr))