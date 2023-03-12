while True:    
    grade=float(input("輸入你的分數"))
    if 0<=grade<=100:
        print('你輸入的數字')
        if grade>=60:
            print("你有及格")
            if grade==100:
                    print('考100，好棒棒喔!')
        elif grade<40:
            print('玩蛋了，BBQ了') 
        else:
            print('要去補考了!')
    else:
        print('你輸入的成績有誤')       