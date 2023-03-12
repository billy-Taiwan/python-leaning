shopping_list=['衣服','鞋子','褲子','外套']
number=1
數量=['3件','8雙','9件','2件']
for a in shopping_list:
    print(number,a)
    number=number+1
查看=int(input('您要查看哪個商品'))
print('{}{}{}{}'.format('您要查看的商品、數量：',shopping_list[查看-1],'要買',數量[查看-1]))             