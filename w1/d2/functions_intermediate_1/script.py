#1
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

#1a
x[1][0]=15

#1b
students[0]['last_name']='Bryant'

#1c
sports_directory['soccer'][0]='Andres'

#1d
z[0]['y']=30

#######################################################################
#2
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(list):
    for x in range(0,len(list)):
        print("First name - " + list[x]['first_name'] + ", Last Name - " + list[x]['last_name'])

#3
def iterateDictionary(key,list):
    for x in range(0,len(list)):
        print(list[x][key])

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

#4
def printInfo(dict):
    for key in dict:
        print()
        print(len(dict[key]),key)
        print()
        for x in range(0,len(dict[key])):
            print(f"{dict[key][x]}")


