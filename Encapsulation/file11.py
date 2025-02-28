class She:
    def __init__(self):
        self._age = int(input("Enter age: "))
        self._stage = input("Enter standard: ") 

class Subject(She): 
    def he(self): 
        print(f"Age: {self._age}, Standard: {self._stage}")

student = Subject()
student.he()
