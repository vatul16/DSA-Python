# Bubble Sort

# It is a comparison-based algorithm in which each pair of adjacent elements is compared
# and the elements are swapped if they are not in order.

def bubbleSort(list):
    # Swap the elements to arrange in order
    for iter_num in range(len(list) - 1, 0, -1):
        for idx in range(iter_num):
            if list[idx] > list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx + 1]
                list[idx + 1] = temp

list = [19, 2, 31, 45, 6, 11, 121, 27]
bubbleSort(list)
print(list)