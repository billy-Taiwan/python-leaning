#群組
class Phone():
    def __init__(self,name,size,price,pixel):
        self.size=size
        self.price=price
        self.pixel=pixel
        self.name=name
    def show_info(self):
        print("手機廠牌",self.name)
        print('手機尺寸',self.size)
        print('手機價格',self.price)
        print('手機像素',self.pixel)
iphone=Phone('蘋果手機',9,45000,12000000)
iphone.show_info()
samsung=Phone('三星手機',10,40000,100000000)
samsung.show_info()

