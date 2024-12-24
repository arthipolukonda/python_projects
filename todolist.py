print("1.add a task \n2.update task \n3.complete a task \n4.delete a task \n5.show existing tasks \n6.exit")
i=True
l=[]
cl=[]
while(i==True):
    a=int(input("enter a command no:"))
    if(a==1):
        t=input("enter a task:")
        l.append(t)
        #print(l)
        i==True
    elif(a==2):
        #print(l)
        for i in range(len(l)):
            print(f"{i+1}.{l[i]}")
        u=input("enter a task to be updated:")
        if(u in l):
            un=input("enter new name of the task:")
            k=l.index(u)
            l[k]=un
        else:
            print("the task no exist in the list")
        i=True
    elif(a==3):
        c=input("enter completed task:")
        cl.append(c)
        l.remove(c)
        i==True
    elif(a==4):
        d=input("enter task to be deleted:")
        if(d in l):
            l.remove(d)
        else:
            print("task do not exit")
        i==True
    elif(a==5):
        print("The current to do list is:")
        if(len(l)!=0):
            for i in range(0,len(l)):
                print(f"{i+1}.{l[i]}")
        else:
            print("None")
        print("The completed tasks are:")
        if(len(cl)!=0):
            for j in range(0,len(cl)):
                print(f"{j+1}.{cl[j]}")
        else:
            print("None")
        i=True
    elif(a==6):
        i=False
        print("-*-"*20)
        
        
