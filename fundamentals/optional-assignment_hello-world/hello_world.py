# task 1: print hello world
print("hello world")

#task 2: store name in variable, then print hello {{your name}}
name = 'benji'
print('hello', name)

#task 3: store number in variable, the print hello {{number}} using , concatenation}
number = 42
print('hello', number)

#task 4: store number in variable, then print hello {{number}} using + concatenation
number = 42
print('hello ' + str(number))

# bonus 1: store two favorite foods in variables and print string 'I love to eat {} and {}' with format method
food1 = 'soup'
food2 = 'salad'
print('I like to eat {} and {}'.format(food1, food2))

# bonus 2: store two favorite foods in variables and print string 'I love to eat {} and {}' with f string method
food1 = 'soup'
food2 = 'salad'
print(f'I like to eat {food1} and {food2}')

# bonus 3
food1 = 'soup'
food2 = 'salad'
print('I like to eat %s and %s' % (food1, food2))