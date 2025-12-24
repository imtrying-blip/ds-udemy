def mergeSortedArrays(arr1, arr2):
    return sorted(arr1 + arr2)

print(mergeSortedArrays([2,1,9], [6,4,8,5,7,1]))

# def mergeSortArrays(arr1, arr2):
#     mergedArr = arr1 + arr2
#     mergedSortedArr = []
#     i=len(mergedArr) - 1
#     for num in mergedArr:
#         if len(mergedSortedArr) == 0:
#             mergedSortedArr.append(num)
        
#         elif num >= mergedSortedArr[i]:
#             mergedSortedArr.append(num)

#         else:
#             while num < mergedSortedArr[i]:
#                 i-=1
#                 if num > mergedSortedArr[i]:
#                     mergedSortedArr.append(num)
#     return mergedSortedArr


# 1,2,9
# 6

def mergeSortArrays(arr1, arr2):
    merged = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Add remaining elements
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])

    return merged

print(mergeSortArrays([2,1,9], [6,4,8,5,7,1]))

