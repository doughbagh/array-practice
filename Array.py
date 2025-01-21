array_list = [10, 7, 5, 8, 11, 9] # Array list

# Output all array values:
for number in array_list:
    print(number)

# Looking for value 5 in the array list:
for i in range(len(array_list)):
    if array_list[i] == 5:
        print("Value 5 found at index:", i) # Output the index of value 5

# Looking for value 9 in the array list:
for i in range(len(array_list)):
    if array_list[i] == 9:
        print("Value 9 found at index:", i)

# Looking for an array which is not existant in the array list:
for i in range(len(array_list)):
    if array_list[i] == 2:
        print("Value 2 found at index:", i)
    else:
        print("Value 2 not found in the array list")
        break

# Output the array list in reverse order:
array_list.sort(reverse=True) # Sorting the array in reverse order
print("Array list in descending order: ", array_list) # Output the array list in reverse order

# Output the array list in ascending order:
array_list.sort() # Sorting the array in ascending order
print("Array list in ascending order:", array_list) # Output the array list in ascending order
