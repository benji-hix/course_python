# 1: update values in dictionaries and lists
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30


# 2: iterate through a list of dictionaries 

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


def iterate_dictionary(students):
    for object in students:
        for key, val in object.items():
            print(key, "-", val)


# 3: create function that, given list of dictionaries and key name,
# print the value stored in that key for each dictionary


def iterate_dictionary_2(key_name, some_list):
    for object in some_list:
        print(object[key_name])

iterate_dictionary_2('first_name', students)

# 4: iterate through dictionary with list values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def print_info(some_dictionary):
    for key, value in some_dictionary.items():
        print ('\n', str(len(value)), key.upper(), '\n')
        for element in value:
            print(element)


print_info(dojo)