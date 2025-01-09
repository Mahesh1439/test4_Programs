"""
pattern:-13
2	4	6	8	10
1	3	5	7	9
2	4	6	8	10
1	3	5	7	9
2	4	6	8	10
1	3	5	7	9
2	4	6	8	10
1	3	5	7	9
2	4	6	8	10
1	3	5	7	9"""



for i in range(1,11):
    even=2
    odd=1
    for j in range(1,6):
        if i%2==1:  
            print(even,end=" ") 
        even=even+2
        if i%2==0:
            print(odd,end=" ") 
        odd=odd+2
    print()