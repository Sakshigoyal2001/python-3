test=int(input())
for i in range(1,test+1):
    tables,people=map(int,input().split())
    if(tables>=people):
        print(1)
    else:
        PA=people//tables
        PB=PA+1
        TB=people%tables
        TA=tables-TB
        facto=list((1,1))
        for i in range(2,people+2):
            x=i*facto[i-1]
            facto.append(x)
        divide=facto[people]//((facto[PA]**TA)*(facto[PB]**TB)*facto[TA]*facto[TB])
        if(PB>=4):
            arrange=int(divide*(facto[PA-1]/2)**TA*(facto[PB-1]/2)**TB)
        else:
            arrange=divide
        print(arrange)
