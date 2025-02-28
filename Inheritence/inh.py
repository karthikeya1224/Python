class bird:
    def name(self):
        print("golden sparrow")
class animal(bird):
    def species(self):
        print("lion")

d=animal()
d.name()
d.species()