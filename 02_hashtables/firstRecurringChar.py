# //Google Question
# //Given an array = [2,5,1,2,3,5,1,2,4]:
# //It should return 2

# //Given an array = [2,1,1,2,3,5,1,2,4]:
# //It should return 1

# //Given an array = [2,3,4,5]:
# //It should return undefined

def firstRecurringChar(arr):
    seen_chars=set()
    for char in arr:
        if char in seen_chars:
            return char
        else:
           seen_chars.add(char)

print(firstRecurringChar([2,5,1,2,3,5,1,2,4]))
print(firstRecurringChar([2,1,1,2,3,5,1,2,4]))
print(firstRecurringChar([2,5,5,2,3,5,1,2,4]))


# Test cases
assert firstRecurringChar([2,5,1,2,3,5,1,2,4]) == 2
assert firstRecurringChar([2,1,1,2,3,5,1,2,4]) == 1
assert firstRecurringChar([2,3,4,5]) is None
assert firstRecurringChar([2,5,5,2,3,5,1,2,4]) == 5  # bonus case
assert firstRecurringChar([]) is None  # empty array
assert firstRecurringChar([1]) is None  # single element
assert firstRecurringChar([1,1,2,3]) == 1  # recurring at start
assert firstRecurringChar([1,2,3,1]) == 1  # recurring at end
assert firstRecurringChar([2,2,2,2]) == 2  # all same elements
assert firstRecurringChar([1,2,3,4,5,1,2]) == 1  # multiple recurrences, first is 1

print("All test cases passed!")


# //Bonus... What if we had this:
# // [2,5,5,2,3,5,1,2,4]
# // return 5 because the pairs are before 2,2