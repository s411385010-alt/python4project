n = int(input())
score = {}

for _ in range(n):
    name, status = input().split()
    if status=="AC":
       score[name]=score.get(name,0)+1
       
    

max_score = 0
ans = ""

for name in score:
    if score.get(name)>max_score:
       max_score=score[name]
       ans=name

print(ans)

   
     
        

