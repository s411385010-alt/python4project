my_list=[];
attendance=0;
number=int(input()) #使用者輸入 範圍1-number間的數字


line=input()
    
my_list=line.split()
  
    
for k in set(my_list):
       freq=my_list.count(k);#數mylist的k值
       if(freq%2==1):
         attendance+=1;
         
       
       
print(attendance);
