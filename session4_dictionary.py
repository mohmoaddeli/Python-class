print('give the name and age for three person \n')
print('person1')
name1 = input("name: ")
age1 = input("age: ")
print()
print('person2')
name2 = input("name: ")
age2 = input("age: ")
print()
print('person3')
name3 = input("name: ")
age3 = input("age: ")

d = {name1: age1, name2: age2, name3: age3}

list1 = list((d.values()))

print('------------------------')
print()
print('The name of the oldest person(s) is(are):\n')
if max((list1[0]), (list1[1]), (list1[2])) == d[name1]:
    print(name1)
if max((list1[0]), (list1[1]), (list1[2])) == d[name2]:
    print(name2)
if max((list1[0]), (list1[1]), (list1[2])) == d[name3]:
    print(name3)
