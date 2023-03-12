shopping_list=['衣服','鞋子','褲子','外套']
number=1
數量=['3件','8雙','9件','2件']
for a in shopping_list:
    print(number,a)
    number=number+1
查看=(input('您要查看哪個商品'))
if 查看==shopping_list[0] or 查看==shopping_list[1] or 查看==shopping_list[2] or 查看==shopping_list[3] :
    if 查看==shopping_list[0]:
        print('您要查看的商品、數量',shopping_list[0],'要買',數量[0])
    if 查看==shopping_list[1]:
        print('您要查看的商品、數量',shopping_list[1],'要買',數量[1])
    if 查看==shopping_list[2]:
        print('您要查看的商品、數量',shopping_list[2],'要買',數量[2])
    if 查看==shopping_list[3]:
        print('您要查看的商品、數量',shopping_list[3],'要買',數量[3])
else:
    print('您的輸入錯誤')