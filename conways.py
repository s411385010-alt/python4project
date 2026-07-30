def sum_neighbors(status,x,y,n,m):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  ( 0, -1),          ( 0, 1),
                  ( 1, -1), ( 1, 0), ( 1, 1)]
    total=0
    for dx, dy in directions:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<m:
         total+=status[nx][ny]
    return total


def conway(status,n,m):
      new_status=[[0 for _ in range(m)] for _ in range(n)]
      
      for i in range(n):

         for j in range(m):
            cnt=sum_neighbors(status,i,j,n,m)
            if status[i][j]==1 and (cnt!=2 and cnt!=3):
                new_status[i][j]=0

            elif status[i][j]==0 and (cnt==3):
                new_status[i][j]=1#此處必須用new_status 去更新,用舊的資料會混在一起

                #數總和,其餘情況維持0不需動作
         return status
             

line=input()
n,m=map(int,line.split())
initial_list=[[0 for _ in range(m)] for _ in range(n)] #_表示用不到
for i in range(n):
    row=list(map(int, input().split()))#row 為list輸入
    for j in range(m):
        initial_list[i][j]=row[j]#將intital_test 賦值


L=int(input())

for k in range(L):
    a=int(input())
    status = [row[:] for row in initial_list] #對每次詢問複製原始盤面(要從原始盤面開始推)
    for step in range(a):
        status=conway(initial_list,n,m)
        
    s=":"
    print(f"{a}:")#f-string 格式化字串
    for row in status:
        print(*row)#讓row之間換行
