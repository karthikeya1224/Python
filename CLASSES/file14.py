class info:
    def data(self):
        self.name=input('enter name:')
        self.age=int(input("enter age:"))
        self.location=input("enter location:")
    def save(self):
        print(f"Name:{self.name},Age:{self.age},Location:{self.location}")
person=info()
person.data()
person.save()