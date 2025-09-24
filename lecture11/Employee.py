class Employee:
    def __init__(self):
        self.__maxearn = 30000
    def earn(self):
        print("earning is : {}".format(self.__maxearn))
    def setmaxearn(self, earn):
        self.__maxearn = earn
emp1 = Employee()
emp1.earn()

emp1.setmaxearn(10000)
emp1.earn()
emp1.setmaxearn(15000)  
emp1.earn()