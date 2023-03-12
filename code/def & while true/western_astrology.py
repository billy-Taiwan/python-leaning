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