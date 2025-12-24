# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
def containsDuplicate(arr):
    seen_numbers=set()
    for num in arr:
        if num in seen_numbers:
            return True
        seen_numbers.add(num)
    return False


# Test cases
assert containsDuplicate([1,2,3,4]) == False  # no duplicates
assert containsDuplicate([1,2,2,3]) == True   # duplicate 2
assert containsDuplicate([]) == False         # empty array
assert containsDuplicate([1]) == False        # single element
assert containsDuplicate([1,1,1]) == True     # all same
assert containsDuplicate([1,2,3,1]) == True   # duplicate at end
assert containsDuplicate([2,1,3,4,2]) == True # duplicate not consecutive

print("All test cases passed!")
