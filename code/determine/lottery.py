import random
回答=int(input('請輸入一個介於1~10000的數字'))
特別獎=random.randint(1,10000)
特獎=random.randint(1,10000)
頭獎=random.randint(1,10000)
二等獎=random.randint(1,10000)
三等獎=random.randint(1,10000)
count=0
獎金=[10000000,2000000,200000,50000,10000]
while True:
    if 回答==特別獎:
        print('{}{}{}'.format('恭喜您獲得特別獎','您的獎金=',獎金[0]))
        print('{}{}{}'.format('你總共猜了',count,'次'))
        break
    elif 回答==特獎:
        print('{}{}{}'.format('恭喜您獲得特獎','您的獎金=',獎金[1]))
        print('{}{}{}'.format('你總共猜了',count,'次'))
        break
    elif 回答==頭獎:
        print('{}{}{}'.format('恭喜您獲得頭獎','您的獎金=',獎金[2]))
        print('{}{}{}'.format('你總共猜了',count,'次'))
        break
    elif 回答==二等獎:
        print('{}{}{}'.format('恭喜您獲得二等獎','您的獎金=',獎金[3]))
        print('{}{}{}'.format('你總共猜了',count,'次'))
        break
    elif 回答==三等獎:
        print('{}{}{}'.format('恭喜您獲得三等獎','您的獎金=',獎金[4]))
        print('{}{}{}'.format('你總共猜了',count,'次'))
    else:
        if 回答>特別獎:
            print('{}{}{}'.format('回答','大於','特別獎'))
            if count==9:
                print('銘謝惠顧')
                break
            else:
                count=count+1 
        elif 回答<特別獎:
            print('{}{}{}'.format('回答','小於','特別獎'))
            if count==9:
                print('銘謝惠顧')
                break
            else:
                count=count+1 
        elif 回答>10000 or 回答<0:
            print('您的輸入有誤')
            if count==9:
                print('銘謝惠顧')
                break
        elif 回答>特獎:
            print('{}{}{}'.format('回答','大於','特獎'))
            if count==9:
                print('銘謝惠顧')
                break
            else:
                回答=int(input('請輸入一個介於1~10000的數字'))
                count=count+1 
        elif 回答<特獎:
            print('{}{}{}'.format('回答','小於','特獎'))
            if count==9:
                print('銘謝惠顧')
                break
            else:
                回答=int(input('請輸入一個介於1~10000的數字'))
                count=count+1 
        elif 回答>10000 or 回答<0:
            print('您的輸入有誤')
            if count==9:
                print('銘謝惠顧')
                break 
        elif 回答>頭獎:
            print('{}{}{}'.format('回答','大於','頭獎'))
            if count==9:
                print('銘謝惠顧')
                break
            else:
                count=count+1
        elif 回答<頭獎:
            print('{}{}{}'.format('回答','小於','頭獎'))
            if count==9:
                print('銘謝惠顧')
                break
            else:
                count=count+1 
        elif 回答>10000 or 回答<0:
            print('您的輸入有誤')
            if count==9:
                print('銘謝惠顧')
                break
        elif 回答>二等獎:
            print('{}{}{}'.format('回答','大於','二等獎'))
            if count==9:
                print('銘謝惠顧')
                break
            else:
                count=count+1 
        elif 回答<二等獎:
            print('{}{}{}'.format('回答','小於','二等獎'))
            if count==9:
                print('銘謝惠顧')
                break
            else:
                回答=int(input('請輸入一個介於1~10000的數字'))
                count=count+1 
        elif 回答>10000 or 回答<0:
            print('您的輸入有誤')
            if count==9:
                print('銘謝惠顧')
                break
        elif 回答>三等獎:
            print('{}{}{}'.format('回答','大於','三等獎'))
            if count==9:
                print('銘謝惠顧')
                break
            else:
                count=count+1 
        elif 回答<三等獎:
            print('{}{}{}'.format('回答','小於','三等獎'))
            if count==9:
                print('銘謝惠顧')
                break
    回答=int(input('請輸入一個介於1~10000的數字'))