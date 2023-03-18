shopping_list=[]
print('清單',shopping_list)
def Addition():    
    add=input('請輸入您要新增的項目')
    shopping_list.append(add)
    print('清單',shopping_list)
def subtraction():    
    remove=input('請輸入您要新增的項目')
    shopping_list.remove(remove)
    print('清單',shopping_list)
def search():
    number=1
數量=['3件','8雙','9件','2件']
for a in shopping_list:
    print(number,a)
    number=number+1
查看=int(input('您要查看哪個商品'))
print('{}{}{}{}'.format('您要查看的商品、數量：',shopping_list[查看-1],'要買',數量[查看-1]))   
while True:
    a=input('您要新增還是刪減(新增打+，刪減打-，都不要就打no)')
    if a=="+":
        Addition()
    elif a=="-":
        subtraction()
    else:
        break


    
    

