class student:
    def __init__(self,name,age,attendance):
        self.name=name
        self.age=age
        self.attendance=attendance
    def info(self):
        print(f"{self.name},{self.age} {self.attendance}")
data=student('karthik',22,75)
data.info()