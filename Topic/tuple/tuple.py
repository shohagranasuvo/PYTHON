my_tuple=('chanel', 'mitch', 'sara', 'cynthia', 'diane', 'steeve')
print(my_tuple[:])


print(my_tuple[-1])
print(my_tuple[-1],my_tuple[-2])

tuple1 = ("SHOHAG" ,"RANA" ,23)
print(type(tuple1))
print(len(tuple1))

my_tuple = ("hello", [87, 40, 60], "world", (10, 25, 30))

print(my_tuple[1][1],my_tuple[2] , my_tuple[1],my_tuple[3])


my_tuple = ('math','science','science','python','english')
found =False
for value in my_tuple:
    
     if value=='python':
         found=True 
         break
                    #   print("FOUND")


if(found):
    print(value +"  found")
    
else:
    print("NOT FOUND ")



