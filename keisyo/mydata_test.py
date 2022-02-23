from datalog import Datalog

class Mydata(Datalog):
    def printlog(self):
        for date, data in self.loglist:
            print(date, data)

obj = Mydata()
obj.log("hello")
obj.log("afternoon")
obj.printlog()