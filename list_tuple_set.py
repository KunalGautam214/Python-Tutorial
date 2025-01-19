nums = [3, 1, 2, 4, 5]

print(nums)

print(len(nums))  # length of the nums list

print(nums[0])
print(nums[len(nums) - 1])
print(nums[-1])  # last element of the nums list
print(nums[-2])
print(nums[0:2])  # list slicing from 0 to 2, where 0 is inclusive and 2 is exclusive index
print(nums[:2])
print(nums[2:])

nums = [3, 1, 2, 4, 5]
nums.append(6)
print(nums)  # nums list after appending 6
nums.insert(0, 7)  # nums list after inserting 7 at index 0
print(nums)

# difference between append and extend methods
list_2 = [7, 9, 8]
nums.append(list_2)
print(nums)
nums.extend(list_2)
print(nums)

# difference between remove and pop methods
nums = [3, 1, 2, 4, 5]
nums.remove(5)
# nums.remove(7) # throw error because 7 is not present in nums list
print(nums)
popped = nums.pop()
print(popped)
print(nums)

nums = [3, 1, 2, 4, 5]
nums.reverse()
print(nums)  # reverse list
nums.sort()  # sorting list in ascending order inline
print(nums)
nums.sort(reverse=True)  # sorting list in descending order inline
print(nums)

sorted_list = sorted(nums)  # sorting list in ascending order
print(sorted_list)
sorted_list = sorted(nums, reverse=True)  # sorting list in descending order
print(sorted_list)
print(nums)

print(min(nums))
print(max(nums))
print(sum(nums))

print(nums.index(5))  # finding index value of 5
print(5 in nums)

for item in nums:
    print(item)

courses = ['History', 'Art', 'CompSci', 'Design']
print(courses)
new_courses = ', '.join(courses)  # converting list to string using comma separated
list_courses = new_courses.split(', ')  # converting string to list using comma separated
print(new_courses)
print(list_courses)

# mutable
list_1 = [1, 2, 3, 4, 5]
list_2 = list_1
list_1[0] = 6
print(list_1)
print(list_2)

# Immutable
tuple_1 = (1, 2, 3, 4, 5)
tuple_2 = tuple_1
# tuple_1[0] = 6
for item in tuple_1:
    print(item)

sets = {1, 3, 5, 6, 7}
print(sets)

print(6 in sets)

sets_1 = {5, 6, 7, 10, 11}
print(sets.intersection(sets_1))  # finding common elements present in both sets
print(sets.difference(sets_1))  # finding different elements which are not present in 2nd set
print(sets.union(sets_1))  # joining all the elements of set 1 and set 2

# empty list
empty_list = []
empty_list = list()

# empty tuple
empty_tuple = ()
empty_tuple = tuple()

# empty sets
empty_set = {}  # This is not right! It's a dict
empty_set = set()
