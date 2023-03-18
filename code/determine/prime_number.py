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

prime_number()