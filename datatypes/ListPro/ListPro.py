list1 = ["Rohan", "Physics", 21, 69.75]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
list4 = [25.50, True, -55, 1+2j]
print(list1)
print(list2)


list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])


"""
"""

#1. Find the Sum of All Elements in a List

numbers = [10, 20, 30, 40]
total = sum(numbers)
print("Sum:", total)


#3. Find the Largest and Smallest Element

numbers = [3, 8, 1, 6, 0, 9]
print("Max:", max(numbers))
print("Min:", min(numbers))

#4 4. Reverse a List

my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
print("Reversed:", reversed_list)

#6. Remove Duplicates from a List
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print("Unique:", unique_numbers)

#7.8. Check if an Element Exists in a List

items = ['pen', 'pencil', 'eraser']
if 'pencil' in items:
    print("Found pencil")
else:
    print("Pencil not found")

# Count Occurrences of an Element
colors = ['red', 'blue', 'red', 'green', 'red']
print("Red count:", colors.count('red'))

#
