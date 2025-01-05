student_details = [
  {'student_id' : 1, 'subject' : 'math', 'midterm' : 60, 'final' : 85},
  {'student_id' : 2, 'subject' : 'math', 'midterm' : 80, 'final' : 78},
  {'student_id' : 3, 'subject' : 'math', 'midterm' : 90, 'final' : 85}
]

avg1=( (student_details[0]["midterm"])+(student_details[0]["final"]))/2
avg2=( (student_details[1]["midterm"])+(student_details[1]["final"]))/2
avg3=( (student_details[2]["midterm"])+(student_details[2]["final"]))/2

student_avg=[{"Student_ID":1 , "avg":avg1},
             {"Student_ID":2, "avg":avg2},
             {"Student_ID":3 , "avg":avg3}
    
]
from pprint import pprint
pprint(student_avg)


my_salary = {"alex": 25, "sally": 28, "dina": 30}
names= list(my_salary.keys())
sala=list((my_salary.values()))

x=sum((my_salary.values()))
print(names ,sala ,x)

my_dictionary = {"Key 1": 20, "Key 2": 30, "Key 3": 50}
result =dict((key,value) for key , value in my_dictionary.items() if value<=30)
print (result)

my_set={3,2,1,4,3,2}
print(my_set)

my_list =[1,3,2,4,3,2]
print(my_list)
my_set1 =set(my_list)
print(my_set1)


