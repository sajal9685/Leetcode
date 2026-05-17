n=int(input("enter number =" ))
li =[]
for i in range(1,n+1):
    if i%3 ==0  and i%5== 0: 
        li.append("fizzbuzz")
        print("fizzbuzz")
    elif i%5 == 0:
        li.append("buzz")
        print ("buzz")  
    elif i%3 ==0:
        li.append("fizz")
        print ("fizz")
    else :
        li.append(str(i))
        print(str(i))  
print(li)