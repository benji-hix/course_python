# function 1 countdown
# create function that accepts a number as an argument
# return a new list that counts down by one, from the number, down to 0

def countdown(number):
    new_list = []
    for i in range(number, -1, -1):
        new_list.append(i)
    return new_list

print(countdown(5))

# function 2 print and return
# create a function that will receive a list with two numbers. Print the first value and return second

def print_and_return(list):
    print(list[0])
    return list[1]

print(print_and_return([3,4]))

# function 3 first plus length
# create a fnuction that accepts a list and returns the sum of the first value in the list
# plus the list's length 

def first_plus_length(list):
    return list[0] + len(list)

print(first_plus_length([2, 3, 4, 5]))

# function 4 values greater than second
# write function that accepts list and creates new list
# containing only the values from the original list that are greater than its 2nd value
# print how many values this is then return new list
# if list has less than 2 elements, return false

def greater_than_second(list):
    if len(list) < 0:
        return False
    else:
        newList = []
        count = 0
        for i in list:
            if i > list[1]:
                newList.append(i)
                count += 1
    print(count)
    return newList

print(greater_than_second([1, 3, 5, 6, 2]))

#function 5 this length, that value
# write a function that accepts two integers as parameters: size and value
# create and return a list whose length is equal to give size, and whose values are the given value

def length_and_value(length, value):
    listNew = []
    for i in range(0, length):
        listNew.append(value)
    return listNew

print(length_and_value(4, 5))