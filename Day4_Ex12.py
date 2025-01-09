"""pattern:-11
pattern:-10
1	2	3	4	5
5	4	3	2	1	
1	2	3	4	5
5	4	3	2	1
1	2	3	4	5"""

n=0
for i in range(5):
    for j in range(5):
        if i%2==0:
            n=n+1
            print(n,end=" ")
           
        else:
            print(n,end=" ")
            n=n-1 
    print()









'''for i in range(5,0,-1):
    num1=1
    num2=5
    for j in range(1,6):
        if num1<6:
            print(num1,end=" ")
            num1=num1+1

        print(num2,end=" ")
        num2=num2-1
        
    print()'''

'''for i in range(5):
    num1=1
    num2=5
    for j in range(5):
        if num1<6:
            print(num1,end=" ")
        num1=num1+1
        if num2>0:
            print(num2,end=" ")
        num2=num2-1
        
    print()'''

num1=1
for i in range(5):
    num2=5
    for j in range(1,6):
        print(num1,end=" ")
        num1=num1+1
        if num1>5:
            num1=5
            num1=num1-1
        
    print()
