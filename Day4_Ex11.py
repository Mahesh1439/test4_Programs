"""pattern:-11
pattern:-10
1	2	3	4	5	1	2	3	4	5
1	2	3	4	5	1	2	3	4	5
1	2	3	4	5	1	2	3	4	5
1	2	3	4	5	1	2	3	4	5
1	2	3	4	5	1	2	3	4	5
1	2	3	4	5	1	2	3	4	5
1	2	3	4	5	1	2	3	4	5
1	2	3	4	5	1	2	3	4	5
1	2	3	4	5	1	2	3	4	5
1	2	3	4	5	1	2	3	4	5"""


for i in range(10):
    num=1
    for j in range(10):
        print(num,end=" ")
        num=num+1
        if num>5:
            num=1
        
        '''if num>5:
            num=1
            print(num,end=" ")
        num=num+1'''      
    print()