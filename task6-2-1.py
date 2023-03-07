
lst1=[-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_i,max_i=map(int, input().split())
mas_i=[]
for i in range(len(lst1)):
    if lst1[i]<=max_i and lst1[i]>=min_i:
        mas_i.append(i)
print("Индексы :", (mas_i))
              

