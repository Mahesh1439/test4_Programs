"""
pattern:-14
1	3	5	7	9
2	4	6	8	10
1	3	5	7	9
2	4	6	8	10
1	3	5	7	9
2	4	6	8	10
1	3	5	7	9
2	4	6	8	10
1	3	5	7	9
2	4	6	8	10"""

'''for i in range(1,11):
    num=i
    for j in range(1,6):
        print(num,end=" ")
        num=num+2
        
    print()'''

for i in range(1,11):
    even=2
    odd=1
    for j in range(1,6):
        if i%2==1:
            print(odd,end=" ") 
        odd=odd+2
        if i%2==0:
            print(even,end=" ") 
        even=even+2
    print()