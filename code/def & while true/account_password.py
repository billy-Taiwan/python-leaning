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
        