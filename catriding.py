def simulation(map,size,pos,steps,visited,mistakes):
       #start with S
       si,sj=pos
       
       if si<0 or sj<0 or si>=size or sj>=size:
           return False,-3
       elif (si,sj) in visited:
           return False,-4
       
       elif map[si][sj]=="0" :
           return False,-1
       elif map[si][sj]=="X":
           return False,-2
       

       elif map[si][sj]=="E":
           visited.add((si,sj))
           return True,steps
       elif map[si][sj]=="1" or map[si][sj]=="S":
          visited.add((si,sj))
          return simulation(map,size,(si,sj+1),steps+1,visited,mistakes)
       elif map[si][sj]=="2":
          visited.add((si,sj))
          return simulation(map,size,(si,sj-1),steps+1,visited,mistakes)
       
       elif map[si][sj]=="3":
          visited.add((si,sj))
          return simulation(map,size,(si-1,sj),steps+1,visited,mistakes)
       elif map[si][sj]=="4":
          visited.add((si,sj))
          return simulation(map,size,(si+1,sj),steps+1,visited,mistakes)
       
       


size=int(input())
my_route={}
mistakes=0
steps=0
visited=set()
for i in range(size):
     row=input()
     my_route[i]=row
     for j in range(size):
      
      if row[j]=="S":
          start=(i,j)#tuple
          
      elif row[j]=="E":
          end=(i,j)
valid,count=simulation(my_route,size,start,0,visited,0)
if valid:
    for i in range(size):
     
     for j in range(size):
      if my_route[i][j]!="0" and (i,j) not in visited:
          
          valid=False
    if valid:
        print(count)
    else :
        print("-5")
else :
    print(count)