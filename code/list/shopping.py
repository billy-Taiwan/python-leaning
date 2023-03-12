def shopping():
    shopping_list=['衣服','鞋子','褲子','外套']
    價格=[350,2100,400,750]
    number=1
    for a in shopping_list:
        print(number,a)
        number=number+1
    選擇=(input('請輸入您想要的商品'))
    數量=int(input('請問您想買幾份'))
    if 選擇==shopping_list[0] or 選擇==shopping_list[1] or 選擇==shopping_list[2] or 選擇==shopping_list[3]:
        if 選擇==shopping_list[0]:
            print('您購買的商品、數量和價格:',shopping_list[0],數量,價格[0]*數量)
        if 選擇==shopping_list[1]:
            print('您購買的商品、數量和價格:',shopping_list[1],數量,價格[1]*數量)
        if 選擇==shopping_list[2]:
            print('您購買的商品、數量和價格:',shopping_list[2],數量,價格[2]*數量)
        if 選擇==shopping_list[3]:
            print('您購買的商品、數量和價格:',shopping_list[3],數量,價格[3]*數量)
    else:
        print('您的輸入錯誤')