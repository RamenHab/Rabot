class Homeworks:
    def __init__(self, homework):
        self.__homework=homework

    def getHomework (self):
        return self.__homework   
     
    def setHomework (self, newWork):
            self.__homework=newWork

works=Homeworks("ДЗ")
print(works.getHomework())
works.setHomework("CT")
print(works.getHomework())