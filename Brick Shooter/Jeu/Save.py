
import os
class Save:

    def __init__(self):
        self.vide = "vide"


    def saveTest(self):
        file1 =  open('save.txt', "w+") 
        toFile = ("Write what you want into the field")
        file1.write(toFile)
        file1.close()

    #def loadSave(self):

    


#t=Save()
#t.saveTest()