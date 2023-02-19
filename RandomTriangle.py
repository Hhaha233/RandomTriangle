"""本人初三,这个程序是我在学概率的时候碰到一道题,按照普通解法要列举很多情况写很多字,所以设计了这个程序.
能力还不是很够.请多多包涵"""

list_=[1,2,3,4,5]
total_list=[]
result_list=[]
for a in list_:
    for b in list_:
        if b==a:
            continue
        else:
            for c in list_:
                if c==b or c==a:    
                    continue        #生成序列内和序列中都不重复的三位序列
                else:
                    total_list.append([a,b,c])
# print(total_list)

for i in total_list:
    
    source=[]
    for j in i:     #水平有限,不知道怎么解决内存对应,只能这样搞了
        source.append(j)

    minimum=min(i)
    i.remove(min(i))      #留下最大值和中间值
    # print(i)
    if min(i)+minimum > max(i):        #判定是否为三角形
        result_list.append(source)
# print(result_list)
print("符合条件情况数:",len(result_list),"总结果数:",len(total_list),"概率:",str(round(len(result_list)/len(total_list),4)*100)+"%",sep="  ")
