class Diploma:
    def getdiploma(self):
        print("I got diploma")
class CO(Diploma):
    def getdiploma(self):
        print("i got co diploma")
class IF(Diploma):
    def getdiploma(self):
        print("i got if diploma")
d=Diploma()
c=CO()
i=IF()
d.getdiploma()
c.getdiploma()
i.getdiploma()
