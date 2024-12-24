import random
n=int(input("enter how many games:"))
ac=0
bc=0
for i in range(n):
    print("1.rock\n2.paper\n3.scissors")
    a=int(input("choose one:"))
    b=random.randint(1,3)
    if(a==b):
        print("tie")
    elif((a==1 and b==2)or(a==2 and b==1)or (a==3 and b==1)):
        print("You loose")
        bc+=1
    elif(a==1 and b==3)or (a==2 and b==3) or (a==3 and b==2):
        print("You win")
        ac+=1
    else:
        print("something went wrong")
if(ac>bc):
    print("You won")
elif(ac==bc):
    print("tie")
else:
    print("You loose")
