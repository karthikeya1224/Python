class Father:
    def show_father(self):
        print("Father's property.")
class Mother:
    def show_mother(self):
        print("Mother's property.")

class Child(Father, Mother):
    def show_child(self):
        print("Child's property.")
child1 = Child()
child1.show_father()
child1.show_mother()
child1.show_child()
