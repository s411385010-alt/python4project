my_list=[]

line=input()
my_list=[int(x) for x in line.split()]
number=int(input())
index=0
for a in my_list:
 if a==number:
    print(index)
 index+=1
 


