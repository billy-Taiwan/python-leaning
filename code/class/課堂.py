#課堂資料
import time
class Class():
    def __init__(self,name,homework,teacher,score):
        self.name=name
        self.homework=homework
        self.teacher=teacher
        self.score=score
    def show_info(self):
        print('課堂名稱',self.name)
        print('作業數量',self.homework)
        print('老師名稱',self.teacher)
        print('段考成績',self.score)
    def add_hw (self):
        for a in range (99):
            self.homework+=1 # self. homework = self. homework + 1
            print ( self.homework)
            time.sleep(0.05)

chemistry=Class('化學課',1,'陳俊杰',89)#chemistry.show_info()
chemistry.add_hw()

