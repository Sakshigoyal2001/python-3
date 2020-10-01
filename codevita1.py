a,b=map(int, input().split())
p=int(input())
pg=list(map(float, input().split()))
add_x=0.0
add_y=0.0
for i in range(a):
    add_x=add_x+pg[i]
for i in range(b):
    add_y=add_y+pg[i]
mom_x=20*[0]
mom_y=20*[0]
mom_x[0]=add_x/a
mom_y[0]=add_y/b
j=1
for i in range(a, p):
    j=j+1
    add_x += (-pg[i - a] + pg[i])
    mom_x[j] = add_x/a
j=1
for i in range(b,p):
    j =j+1
    add_y=add_y+(-pg[i - b] + pg[i])
    mom_y[j]=add_y/b

front=0
count=0
if(mom_x[b-a]>mom_y[0] and front==0):
    front=1
if(mom_x[b-a]<mom_y[0]):
    front=-1

for i in range(1,p-b+1):
    if (mom_x[b-a+i] < mom_y[i] and front==1):
        count=count+1
        front=-1
    elif (mom_x[b-a+i]>mom_y[i] and front==-1):
        count=count+1
        front=1
print(count)
