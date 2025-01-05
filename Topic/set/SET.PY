X={1,2,3,4,5,3,2,1,5}
print(X)

y=[1,2,3,4,5,6,5]
z=set(y)
print(z)
check = False
checkFor =10
for iv in X :
    if iv==10 :
        check=True
        print(str(iv) +  " is found ")
        break


if check==False:
    print (  str(checkFor)+" is not found")
    
    
    