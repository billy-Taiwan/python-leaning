def prime_number():
    輸入=int(input('請輸入一個數字'))
    這不是質數=0
    for a in range(1,輸入+1,1):
        if 輸入% a==0:
            這不是質數=這不是質數+1
    if 這不是質數==2:
        print('這是質數') 
    else:
        print('這不是質數') 
def account_password():
    account=input('請輸入您的帳號')
    if account=='123456789@gmail.com' or account=='987654321@gmail.com':
        if account=='123456789@gmail.com':
            password=int(input('請輸入您的密碼'))
            if password==123456789:
                print('歡迎使用本網站')
            else:
                print('您輸入的密碼有誤')
        if account=='987654321@gmail.com':
            password=int(input('請輸入您的密碼'))
            if password==987654321:
                print('歡迎使用本網站')
            else:
                print('您輸入的密碼有誤')
    else:  
        print('查無此帳號')
def western_astrology():
    月份=int(input('請輸入您的出生月份'))
    日期=int(input('請輸入您的出生日期'))
    print('您的生日',月份,日期)
    if 月份==1 or 月份==2 or 月份==3 or 月份==4 or 月份==5 or 月份==6 or 月份==7 or 月份==8 or 月份==9 or 月份==10 or 月份==11 or 月份==12:
        if 月份==1:
            if 日期>=21:
                print('您的星座為水瓶')
            else:
                print('您的星座為魔羯')
        if 月份==2:
            if 日期>=19:
                print('您的星座為雙魚')
            else:
                print('您的星座為水瓶')
        if 月份==3:
            if 日期>=21:
                print('您的星座為牡羊')
            else:
                print('您的星座為雙魚')
        if 月份==4:
            if 日期>=21:
                print('您的星座為金牛')
            else:
                print('您的星座為牡羊')
        if 月份==5:
            if 日期>=22:
                print('您的星座為雙子')
            else:
                print('您的星座為金牛')
        if 月份==6:
            if 日期>=22:
                print('您的星座為巨蟹')
            else:
                print('您的星座為雙子')
        if 月份==7:
            if 日期>=23:
                print('您的星座為獅子')
            else:
                print('您的星座為巨蟹')
        if 月份==8:
            if 日期>=24:
                print('您的星座為處女')
            else:
                print('您的星座為獅子')
        if 月份==9:
            if 日期>=24:
                print('您的星座為天秤')
            else:
                print('您的星座為處女')
        if 月份==10:
            if 日期>=24:
                print('您的星座為天蠍')
            else:
                print('您的星座為天秤')
        if 月份==11:
            if 日期>=23:
                print('您的星座為射手')
            else:
                print('您的星座為天蠍')
        if 月份==12:
            if 日期>=22:
                print('您的星座為摩羯')
            else:
                print('您的星座為射手')
    else:
        print('您輸入的資料有誤')
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

number_number=1
list=[prime_number,account_password,western_astrology,shopping]
for a in list:
    print(number_number,a)
    number_number=number_number+1
step=input("您要執行哪些步驟")
if 

