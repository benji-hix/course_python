# 1) print all integers from 0 to 150
for i in range(0, 151):
    print(i)


# 2) print all multiples of 5 from 5 to 1,000
for i in range(5, 1001, 5):
    print(i)


# 3) print integers 1 to 100 -- if dibisible by 5, print "coding"
# if divisible by 10, print "coding dojo"
for i in range(1, 101):
    if i % 10 == 0:
        print('coding dojo')
    elif i % 5 == 0:
        print('coding')
    else:
        print(i)


# 4) add odd integers from 0 to 500,000 and print final sum 
sum = 0
for i in range(0, 500001):
    if i % 2 != 0:
        sum += i
print(sum)


# 5) print positive numbers starting at 2018, counting down by fours
for i in range(2018, 0, -4):
    print(i)


# 6) set lowNum, highNum, mult.
# start at lowNum and, going through highNum, print only integers that
# are a multiple of mult.
low_num = 2
high_num = 9
mult = 3
for i in range(low_num, (high_num + 1)):
    if i % mult == 0:
        print(i)