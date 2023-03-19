#自我介紹
class Introdution():
    def __init__(self,name,age,interest):
       self.name=name
       self.age=age
       self.interest=interest
    def show_info(self):
        input("請輸入您的名字",self.name)
        int(input("請輸入您的年紀",self.age))
        input("請輸入您的興趣",self.interest)
print('歡迎使用自我介紹產生器')
me=Introdution('楊以理',15,'閱讀國際新聞')
print('大家好，我是{}，今年{}，喜歡{}，很高興認識大家。'.format(me.name,me.age,me.interest))
