
#1
names = ["sara", "chanel", "mike", "ryan", "holy", "alex", "rob"]
print(names[0],names[1],names[-1])

#2
names = ["sara", "chanel", "mitch", "ryan", "holy", "alex", "rob"]
print(names[-3:] )
print(names[:])
print(names[1:4] ,names[0:3])
print(names[::2])

#3
my_list = ["Mitch", ["sara", "sally", "joe"], "peter", "aly"]
print(my_list[1][1])

print(my_list[1])
print(my_list[-1])
print(my_list[3])

#4
my_list = ["Mitch", ["sara", "sally", "joe"], "peter", "aly"]
print(len(my_list))
my_list.append("SHOHAG")
print(my_list)

#5

my_list = ["Mitch", ["sara", "sally", "joe"], "peter", "aly"]
my_list.remove("peter")
print(my_list)
del my_list[-1]
print(my_list)

#6

my_list = [50, 20, 30, 10, 40, 15, 45]

my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)

#7
grocery_list = [['chips','jelly','chocolate'],['sweet potatoes','potatoes'],['peanuts','protein bar']]
print(grocery_list[0][-1],grocery_list[1][-1],grocery_list[2][-1])

#8
friendName= ["JIMEL","SAJID","SADDIB","MARUF"]
friendName.sort()
print(friendName)


