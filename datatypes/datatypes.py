# x = input()
# print(type(x))
# dict
students=[]
for i in range(3):
    student={}
    name=input('enter name ').strip().upper()
    age=int(input("enter age "))
    city=input('enter city kat').strip().upper()
    student={
        "name": name, "age": age , "city": city
    }
    students.append(student)
for i in students:
    print(i,end=" ")
